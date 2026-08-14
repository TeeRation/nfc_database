from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Location, NfcTag
from app.schemas import (
    LocationData,
    LocationResolveRequest,
    LocationResolveResponse,
)


router = APIRouter(
    prefix="/api/location",
    tags=["Location"],
)


@router.post(
    "/resolve",
    response_model=LocationResolveResponse,
)
def resolve_location(
    request: LocationResolveRequest,
    db: Session = Depends(get_db),
) -> LocationResolveResponse:
    nfc_tag = db.get(NfcTag, request.tag_id)

    if nfc_tag is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="NFC-метка не найдена.",
        )

    if nfc_tag.is_active != 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="NFC-метка неактивна.",
        )

    if nfc_tag.entity_type != "location":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="NFC-метка не привязана к местоположению.",
        )

    if nfc_tag.entity_id is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="У NFC-метки отсутствует идентификатор объекта.",
        )

    location = db.get(Location, nfc_tag.entity_id)

    if location is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Местоположение, связанное с NFC-меткой, не найдено.",
        )

    if location.is_active != 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Местоположение неактивно.",
        )

    return LocationResolveResponse(
        tag_id=nfc_tag.id,
        entity_type=nfc_tag.entity_type,
        location=LocationData(
            id=location.id,
            name=location.name,
            description=location.description,
            is_active=location.is_active,
        ),
    )