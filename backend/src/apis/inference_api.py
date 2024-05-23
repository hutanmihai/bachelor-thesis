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
from src.translation import translation_mapping_custom_options

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
        # Translate optional fields, and append them to the description
        translated_fields = inference_schema.translate_optional_fields()
        inference_schema.audio_and_technology = translated_fields["Audio and technology"]
        inference_schema.comfort_and_optional_equipment = translated_fields["Comfort and optional equipment"]
        inference_schema.electronics_and_assistance_systems = translated_fields["Electronics and assistance systems"]
        inference_schema.performance = translated_fields["Performance"]
        inference_schema.safety = translated_fields["Safety"]

        def concatenate_custom_options():
            custom_options_string = ""
            for key, value in translated_fields.items():
                if len(value) > 0:
                    custom_options_string = custom_options_string + f"{translation_mapping_custom_options[key].lower()}: {', '.join(value)}\n"
            return custom_options_string

        new_description = concatenate_custom_options() + inference_schema.description

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
            description=new_description,
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
                description=new_description,
                image_url=inference_schema.image_url,
                prediction=prediction,
                user_id=user_id,
            )
        )
        return InferenceResponseSchema(prediction=prediction)
    except Exception as e:
        return generate_api_error_response(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e))
