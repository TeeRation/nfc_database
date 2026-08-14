from app.models import Location, NfcManufacturer, NfcTag


def test_resolve_location_success(client, db):
    manufacturer = NfcManufacturer(
        id="manufacturer-test",
        name="Тестовый производитель",
        description=None,
        is_active=1,
    )

    tag = NfcTag(
        id="tag-test-1",
        entity_id="location-test-1",
        entity_type="location",
        manufacturer_id="manufacturer-test",
        is_active=1,
    )

    location = Location(
        id="location-test-1",
        name="Тестовая локация",
        description="Локация для pytest",
        nfc_tag_id="tag-test-1",
        is_active=1,
    )

    db.add(manufacturer)
    db.flush()

    db.add(tag)
    db.flush()

    db.add(location)
    db.commit()

    response = client.post(
        "/api/location/resolve",
        json={
            "tag_id": "tag-test-1",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["tag_id"] == "tag-test-1"
    assert data["entity_type"] == "location"
    assert data["location"]["id"] == "location-test-1"
    assert data["location"]["name"] == "Тестовая локация"
    assert data["location"]["is_active"] == 1


def test_resolve_reserved_tag(client, db):
    manufacturer = NfcManufacturer(
        id="manufacturer-test",
        name="Тестовый производитель",
        description=None,
        is_active=1,
    )

    tag = NfcTag(
        id="tag-test-2",
        entity_id=None,
        entity_type=None,
        manufacturer_id="manufacturer-test",
        is_active=1,
    )

    db.add(manufacturer)
    db.flush()

    db.add(tag)
    db.commit()

    response = client.post(
        "/api/location/resolve",
        json={
            "tag_id": "tag-test-2",
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": "NFC-метка не привязана к местоположению."
    }