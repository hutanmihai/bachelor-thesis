from uuid import UUID

from fastapi import APIRouter, Depends, status
from src.apis.utils.utils import generate_api_error_response, generate_error_responses
from src.auth.auth_bearer import auth_required
from src.models import Entry
from src.schemas.errors_schema import ApiError
from src.schemas.inference_schema import InferenceResponseSchema, StructuredDataSchema
from src.services.entry_srv import EntrySrv
from src.services.inference_srv import InferenceSrv

router = APIRouter(tags=["inference"])


@router.post(
    "/inference",
    summary="Inference endpoint",
    description="Inference endpoint",
    status_code=status.HTTP_200_OK,
    response_description="Inference successful",
    responses=generate_error_responses(status.HTTP_403_FORBIDDEN),
    response_model=InferenceResponseSchema,
)
async def inference(
    structured_data_schema: StructuredDataSchema,
    inference_srv: InferenceSrv = Depends(InferenceSrv),
    user_id: UUID = Depends(auth_required),
    entry_srv: EntrySrv = Depends(EntrySrv),
):
    try:
        prediction = await inference_srv.predict(structured_data_schema.dict())
        await entry_srv.create_entry(
            Entry(
                manufacturer=structured_data_schema.manufacturer,
                model=structured_data_schema.model,
                fuel=structured_data_schema.fuel,
                chassis=structured_data_schema.chassis,
                sold_by=structured_data_schema.sold_by,
                gearbox=structured_data_schema.gearbox,
                km=structured_data_schema.km,
                power=structured_data_schema.power,
                engine=structured_data_schema.engine,
                year=structured_data_schema.year,
                description=structured_data_schema.description,
                prediction=prediction,
                user_id=user_id,
            )
        )
        return InferenceResponseSchema(prediction=prediction)
    except Exception as e:
        # TODO: see errors at inference
        print(e)
        return generate_api_error_response(status.HTTP_500_INTERNAL_SERVER_ERROR, "An unexpected error has occured, please try again later")
