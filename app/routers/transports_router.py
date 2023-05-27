from dependency_injector.wiring import inject, Provide, Container
from fastapi import APIRouter, Body, Depends, HTTPException, Path

from app.dto.create_transport import CreateTransport
from app.dto.transport import Transport
from app.dto.update_transport import UpdateTransport
from app.exceptions.already_exists_error import AlreadyExistsError
from app.exceptions.zipcode_not_found_error import ZipcodeNotFoundError
from app.services.transports_service import TransportsService

router = APIRouter()


@router.post(
    '',
    responses={200: {'description': 'Create transport',
                     'model': Transport},
               400: {'description': 'number should be unique'}}
)
@inject
async def create_transport(
        body: CreateTransport = Body(),
        transports_service: TransportsService = Depends(Provide[Container.transports_service])
) -> Transport:
    try:
        return await transports_service.create_transport(body)
    except AlreadyExistsError:
        raise HTTPException(status_code=400)


@router.put(
    '/{transport_id}',
    responses={200: {'description': 'Update transport',
                     'model': Transport},
               400: {'description': 'Invalid zipcode'}}
)
@inject
async def update_transport(
        transport_id: int = Path(),
        body: UpdateTransport = Body(),
        transports_service: TransportsService = Depends(Provide[Container.transports_service])
) -> Transport:
    try:
        return await transports_service.update_transport(transport_id, body)
    except ZipcodeNotFoundError:
        raise HTTPException(status_code=400)
