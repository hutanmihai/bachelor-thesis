from uuid import UUID

from fastapi import APIRouter, Depends, status
from src.apis.utils.utils import generate_error_responses
from src.auth.auth_bearer import auth_required
from src.schemas.inference_schema import InferenceResponseSchema, StructuredDataSchema
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
    structured_data_schema: StructuredDataSchema, inference_srv: InferenceSrv = Depends(InferenceSrv), user_id: UUID = Depends(auth_required)
):
    prediction = await inference_srv.predict(structured_data_schema.dict())
    return InferenceResponseSchema(prediction=prediction)
