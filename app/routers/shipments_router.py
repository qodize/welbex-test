from typing import Optional

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, Query, Path, HTTPException, Body

from app.di.containers import Container
from app.dto.create_shipment import CreateShipment
from app.dto.shipment import Shipment
from app.dto.shipments_list_item import ShipmentsListItem
from app.dto.single_shipment import SingleShipment, TransportDistance
from app.dto.update_shipment import UpdateShipment
from app.exceptions.not_found_error import NotFoundError
from app.exceptions.zipcode_not_found_error import ZipcodeNotFoundError
from app.services.shipments_service import ShipmentsService
from app.services.transports_service import TransportsService

router = APIRouter()


@router.get(
    '',
    responses={200: {'description': 'Get list of shipments',
                     'model': list[ShipmentsListItem]}}
)
@inject
async def get_shipments(
        min_weight: Optional[int] = Query(None, description='Minimum weight filter'),
        max_weight: Optional[int] = Query(None, description='Maximum weight filter'),
        max_transport_distance: Optional[int] = Query(450, description='Maximum transport distance filter'),
        shipments_service: ShipmentsService = Depends(Provide[Container.shipments_service]),
        transports_service: TransportsService = Depends(Provide[Container.transports_service])
) -> list[ShipmentsListItem]:
    shipments = await shipments_service.get_shipments(
        min_weight=min_weight,
        max_weight=max_weight,
    )
    transports = await transports_service.get_transports()
    return [
        ShipmentsListItem(
            shipment_id=shipment.shipment_id,
            pick_up_location=shipment.pick_up_location,
            delivery_location=shipment.delivery_location,
            weight=shipment.weight,
            description=shipment.description,
            closest_transports_count=len([
                transport
                for transport in transports
                if await transports_service.distance(
                    transport.current_location,
                    shipment.pick_up_location
                ) <= max_transport_distance
            ])
        )
        for shipment in shipments
    ]


@router.get(
    '/{shipment_id}',
    responses={200: {'description': 'Get one shipment by id',
                     'model': SingleShipment},
               404: {'description': 'Shipment with such id not found'}}
)
@inject
async def get_shipment(
        shipment_id: int = Path(),
        shipments_service: ShipmentsService = Depends(Provide[Container.shipments_service]),
        transports_service: TransportsService = Depends(Provide[Container.transports_service])
) -> SingleShipment:
    try:
        shipment = await shipments_service.get_shipment(shipment_id)
    except NotFoundError:
        raise HTTPException(status_code=404)
    transports = await transports_service.get_transports()
    return SingleShipment(
        shipment_id=shipment.shipment_id,
        pick_up_location=shipment.pick_up_location,
        delivery_location=shipment.delivery_location,
        weight=shipment.weight,
        description=shipment.description,
        transports_distances=[
            TransportDistance(
                number=transport.number,
                distance=await transports_service.distance(
                    transport.current_location,
                    shipment.pick_up_location
                )
            )
            for transport in transports
        ]
    )


@router.post(
    '',
    responses={201: {'description': 'Create shipment',
                     'model': Shipment},
               400: {'description': 'invalid zipcode'}}
)
@inject
async def create_shipment(
        body: CreateShipment = Body(),
        shipments_service: ShipmentsService = Depends(Provide[Container.shipments_service])
) -> Shipment:
    try:
        return await shipments_service.create_shipment(body)
    except ZipcodeNotFoundError:
        raise HTTPException(status_code=400)


@router.put(
    '/{shipment_id}',
    responses={200: {'description': 'Update shipment',
                     'model': Shipment},
               404: {'description': 'Shipment with such id not found'}}
)
@inject
async def update_shipment(
        shipment_id: int = Path(),
        body: UpdateShipment = Body(),
        shipments_service: ShipmentsService = Depends(Provide[Container.shipments_service])
) -> Shipment:
    try:
        return await shipments_service.update_shipment(shipment_id, body)
    except NotFoundError:
        raise HTTPException(status_code=404)


@router.delete(
    '/{shipment_id}',
    responses={200: {'description': 'Delete shipment'},
               404: {'description': 'Not found'}}
)
@inject
async def delete_shipment(
        shipment_id: int = Path(),
        shipments_service: ShipmentsService = Depends(Provide[Container.shipments_service])
):
    try:
        await shipments_service.delete_shipment(shipment_id)
    except NotFoundError:
        raise HTTPException(status_code=404)
