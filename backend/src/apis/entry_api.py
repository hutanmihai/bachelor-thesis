import datetime
from datetime import datetime
from uuid import UUID

from botocore.client import BaseClient
from botocore.exceptions import NoCredentialsError
from fastapi import APIRouter, Depends, File, UploadFile, status
from fastapi.responses import JSONResponse
from src.apis.utils.utils import generate_api_error_response, generate_error_responses
from src.auth.auth_bearer import auth_required
from src.deps import s3_auth
from src.schemas.entry_schema import EntryListSchema, EntrySchema
from src.services.entry_srv import EntrySrv
from src.services.errors import EntryNotCreatedByUser, EntryNotFound
from src.settings import settings

router = APIRouter(tags=["entry"])


@router.get(
    "/entry/all",
    summary="Get all entries",
    status_code=status.HTTP_200_OK,
    response_description="Successfully fetched all entries",
    response_model=EntryListSchema,
    responses=generate_error_responses(status.HTTP_403_FORBIDDEN),
)
async def entry_all(user_id: UUID = Depends(auth_required), entry_srv: EntrySrv = Depends(EntrySrv)):
    entries = await entry_srv.get_all_entries(user_id)
    return EntryListSchema(
        entries=[
            EntrySchema(
                id=entry.id,
                manufacturer=entry.manufacturer,
                model=entry.model,
                fuel=entry.fuel,
                chassis=entry.chassis,
                sold_by=entry.sold_by,
                gearbox=entry.gearbox,
                km=entry.km,
                power=entry.power,
                engine=entry.engine,
                year=entry.year,
                image_url=entry.image_url,
                description=entry.description,
                prediction=entry.prediction,
                user_id=entry.user_id,
            )
            for entry in entries
        ]
    )


@router.delete(
    "/entry/{entry_id}",
    summary="Delete an entry",
    status_code=status.HTTP_200_OK,
    response_description="Successfully deleted the entry",
    responses=generate_error_responses(status.HTTP_404_NOT_FOUND, status.HTTP_403_FORBIDDEN),
)
async def entry_delete(entry_id: UUID, user_id: UUID = Depends(auth_required), entry_srv: EntrySrv = Depends(EntrySrv)):
    try:
        await entry_srv.delete_entry(entry_id, user_id)
    except EntryNotFound:
        return generate_api_error_response(status.HTTP_404_NOT_FOUND, "Entry not found")
    except EntryNotCreatedByUser:
        return generate_api_error_response(status.HTTP_403_FORBIDDEN, "Entry not created by user")
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Entry deleted successfully"},
    )


@router.post(
    "/upload",
    summary="Upload image",
    status_code=status.HTTP_200_OK,
    response_description="Image uploaded successfully",
    responses=generate_error_responses(status.HTTP_400_BAD_REQUEST, status.HTTP_403_FORBIDDEN),
)
async def upload_image(file: UploadFile = File(...), user_id=Depends(auth_required), s3_client: BaseClient = Depends(s3_auth)):
    try:
        if not file.content_type.startswith("image/"):
            return generate_api_error_response(status_code=status.HTTP_400_BAD_REQUEST, detail="File is not an image")

        file_content = await file.read()
        timestamp = str(datetime.timestamp(datetime.now())).split(".")[0]
        file_path = f"images/{user_id}_{timestamp}"

        s3_client.put_object(Body=file_content, Bucket=settings.bucket_name, Key=file_path, ContentType=file.content_type)

        url = f"https://{settings.bucket_name}.s3.amazonaws.com/{file_path}"
        return JSONResponse(status_code=status.HTTP_200_OK, content={"url": url})

    except NoCredentialsError:
        return generate_api_error_response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")
    except Exception as e:
        return generate_api_error_response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
