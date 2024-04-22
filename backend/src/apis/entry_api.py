from uuid import UUID

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from src.apis.utils.utils import generate_error_responses
from src.auth.auth_bearer import auth_required
from src.schemas.entry_schema import EntryListSchema, EntrySchema
from src.schemas.errors_schema import ApiError
from src.services.entry_srv import EntrySrv
from src.services.errors import EntryNotFound

router = APIRouter(tags=["entry"])


@router.get(
    "/entry/all",
    summary="Get all entries",
    status_code=status.HTTP_200_OK,
    response_description="Successfully fetched all entries",
    response_model=EntryListSchema,
    responses=generate_error_responses(status.HTTP_404_NOT_FOUND, status.HTTP_403_FORBIDDEN),
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
        return ApiError(detail="Entry not found")
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Entry deleted successfully"},
    )
