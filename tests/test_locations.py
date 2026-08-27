def test_resolve_location_success(client, location):
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


def test_resolve_reserved_tag(client, reserved_tag):
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