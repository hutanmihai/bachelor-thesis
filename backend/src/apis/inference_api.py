from uuid import UUID

from fastapi import APIRouter, Depends, status
from src.apis.utils.utils import generate_api_error_response, generate_error_responses
from src.auth.auth_bearer import auth_required
from src.models import Entry
from src.schemas.inference_schema import InferenceResponseSchema, InferenceSchema
from src.services.entry_srv import EntrySrv
from src.services.errors import UserNotFound
from src.services.inference_srv import InferenceSrv
from src.services.user_srv import UserSrv

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
    inference_schema: InferenceSchema,
    inference_srv: InferenceSrv = Depends(InferenceSrv),
    user_id: UUID = Depends(auth_required),
    entry_srv: EntrySrv = Depends(EntrySrv),
    user_srv: UserSrv = Depends(UserSrv),
):
    try:
        user = await user_srv.get_user(user_id)
        if user.predictions <= 0:
            return generate_api_error_response(status.HTTP_400_BAD_REQUEST, "No predictions left")
    except UserNotFound:
        return generate_api_error_response(status.HTTP_403_FORBIDDEN, "User not found")
    try:
        prediction = await inference_srv.predict(
            manufacturer=inference_schema.manufacturer,
            model=inference_schema.model,
            fuel=inference_schema.fuel,
            chassis=inference_schema.chassis,
            sold_by=inference_schema.sold_by,
            gearbox=inference_schema.gearbox,
            km=inference_schema.km,
            power=inference_schema.power,
            engine=inference_schema.engine,
            year=inference_schema.year,
            description=inference_schema.description,
            image_url=inference_schema.image_url,
        )
        await user_srv.update_user_predictions(user_id, -1)
        await entry_srv.create_entry(
            Entry(
                manufacturer=inference_schema.manufacturer,
                model=inference_schema.model,
                fuel=inference_schema.fuel,
                chassis=inference_schema.chassis,
                sold_by=inference_schema.sold_by,
                gearbox=inference_schema.gearbox,
                km=inference_schema.km,
                power=inference_schema.power,
                engine=inference_schema.engine,
                year=inference_schema.year,
                description=inference_schema.description,
                image_url=inference_schema.image_url,
                prediction=prediction,
                user_id=user_id,
            )
        )
        return InferenceResponseSchema(prediction=prediction)
    except Exception as e:
        return generate_api_error_response(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e))
