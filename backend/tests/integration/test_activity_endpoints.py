from fastapi.testclient import TestClient


def _activity_payload(
    *,
    name: str = "Actividad 1",
    bac: float = 1000,
    planned_progress: float = 40,
    actual_progress: float = 30,
    actual_cost: float = 250,
) -> dict[str, float | str]:
    return {
        "name": name,
        "bac": bac,
        "planned_progress": planned_progress,
        "actual_progress": actual_progress,
        "actual_cost": actual_cost,
    }


def test_create_activity_successfully(client: TestClient, seeded_project) -> None:
    response = client.post(
        f"/api/v1/projects/{seeded_project.id}/activities",
        json=_activity_payload(),
    )

    assert response.status_code == 201
    body = response.json()
    assert body["id"]
    assert body["project_id"] == str(seeded_project.id)
    assert body["name"] == "Actividad 1"
    assert body["bac"] == 1000
    assert body["planned_progress"] == 40
    assert body["actual_progress"] == 30
    assert body["actual_cost"] == 250
    assert body["created_at"]
    assert body["updated_at"]


def test_return_404_when_creating_activity_for_non_existing_project(client: TestClient) -> None:
    response = client.post(
        "/api/v1/projects/11111111-1111-1111-1111-111111111111/activities",
        json=_activity_payload(),
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Project not found"}


def test_list_activities_by_project_successfully(client: TestClient, seeded_project) -> None:
    create_response = client.post(
        f"/api/v1/projects/{seeded_project.id}/activities",
        json=_activity_payload(name="Actividad lista"),
    )
    assert create_response.status_code == 201

    response = client.get(f"/api/v1/projects/{seeded_project.id}/activities")
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, list)
    assert len(body) == 1
    assert body[0]["name"] == "Actividad lista"
    assert body[0]["project_id"] == str(seeded_project.id)
    assert "evm" in body[0]


def test_get_activity_by_id_successfully(client: TestClient, seeded_project) -> None:
    create_response = client.post(
        f"/api/v1/projects/{seeded_project.id}/activities",
        json=_activity_payload(name="Actividad detalle"),
    )
    activity_id = create_response.json()["id"]

    response = client.get(f"/api/v1/activities/{activity_id}")
    assert response.status_code == 200
    body = response.json()
    assert body["id"] == activity_id
    assert body["name"] == "Actividad detalle"
    assert body["project_id"] == str(seeded_project.id)
    assert "evm" in body


def test_return_404_when_activity_does_not_exist(client: TestClient) -> None:
    response = client.get("/api/v1/activities/11111111-1111-1111-1111-111111111111")
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_update_activity_successfully(client: TestClient, seeded_project) -> None:
    create_response = client.post(
        f"/api/v1/projects/{seeded_project.id}/activities",
        json=_activity_payload(),
    )
    activity_id = create_response.json()["id"]

    update_payload = _activity_payload(
        name="Actividad actualizada",
        bac=1500,
        planned_progress=60,
        actual_progress=50,
        actual_cost=600,
    )
    response = client.put(f"/api/v1/activities/{activity_id}", json=update_payload)

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == activity_id
    assert body["name"] == "Actividad actualizada"
    assert body["bac"] == 1500
    assert body["planned_progress"] == 60
    assert body["actual_progress"] == 50
    assert body["actual_cost"] == 600


def test_delete_activity_successfully(client: TestClient, seeded_project) -> None:
    create_response = client.post(
        f"/api/v1/projects/{seeded_project.id}/activities",
        json=_activity_payload(),
    )
    activity_id = create_response.json()["id"]

    response = client.delete(f"/api/v1/activities/{activity_id}")
    assert response.status_code == 204
    assert response.text == ""

    fetch_response = client.get(f"/api/v1/activities/{activity_id}")
    assert fetch_response.status_code == 404


def test_validate_activity_name_is_required(client: TestClient, seeded_project) -> None:
    response = client.post(
        f"/api/v1/projects/{seeded_project.id}/activities",
        json={"bac": 1000, "planned_progress": 50, "actual_progress": 30, "actual_cost": 200},
    )
    assert response.status_code == 422

    response_empty = client.post(
        f"/api/v1/projects/{seeded_project.id}/activities",
        json=_activity_payload(name="   "),
    )
    assert response_empty.status_code == 422


def test_validate_bac_must_be_greater_than_zero(client: TestClient, seeded_project) -> None:
    response = client.post(
        f"/api/v1/projects/{seeded_project.id}/activities",
        json=_activity_payload(bac=0),
    )
    assert response.status_code == 422


def test_validate_planned_progress_cannot_be_lower_than_zero(
    client: TestClient, seeded_project
) -> None:
    response = client.post(
        f"/api/v1/projects/{seeded_project.id}/activities",
        json=_activity_payload(planned_progress=-1),
    )
    assert response.status_code == 422


def test_validate_planned_progress_cannot_be_greater_than_100(
    client: TestClient, seeded_project
) -> None:
    response = client.post(
        f"/api/v1/projects/{seeded_project.id}/activities",
        json=_activity_payload(planned_progress=101),
    )
    assert response.status_code == 422


def test_validate_actual_progress_cannot_be_lower_than_zero(
    client: TestClient, seeded_project
) -> None:
    response = client.post(
        f"/api/v1/projects/{seeded_project.id}/activities",
        json=_activity_payload(actual_progress=-0.1),
    )
    assert response.status_code == 422


def test_validate_actual_progress_cannot_be_greater_than_100(
    client: TestClient, seeded_project
) -> None:
    response = client.post(
        f"/api/v1/projects/{seeded_project.id}/activities",
        json=_activity_payload(actual_progress=100.1),
    )
    assert response.status_code == 422


def test_validate_actual_cost_cannot_be_negative(client: TestClient, seeded_project) -> None:
    response = client.post(
        f"/api/v1/projects/{seeded_project.id}/activities",
        json=_activity_payload(actual_cost=-1),
    )
    assert response.status_code == 422


def test_verify_activity_response_includes_evm_indicators(
    client: TestClient,
    seeded_project,
) -> None:
    response = client.post(
        f"/api/v1/projects/{seeded_project.id}/activities",
        json=_activity_payload(bac=1000, planned_progress=50, actual_progress=40, actual_cost=300),
    )
    body = response.json()

    assert response.status_code == 201
    evm = body["evm"]
    assert evm["pv"] == 500
    assert evm["ev"] == 400
    assert evm["cv"] == 100
    assert evm["sv"] == -100
    assert evm["cpi"] == 400 / 300
    assert evm["spi"] == 0.8
    assert evm["eac"] == 750
    assert evm["vac"] == 250
    assert evm["cost_status"] == "Eficiente en costos"
    assert evm["schedule_status"] == "Atrasado"


def test_verify_cpi_is_none_when_actual_cost_is_zero(client: TestClient, seeded_project) -> None:
    response = client.post(
        f"/api/v1/projects/{seeded_project.id}/activities",
        json=_activity_payload(actual_cost=0),
    )
    assert response.status_code == 201
    assert response.json()["evm"]["cpi"] is None


def test_verify_spi_is_none_when_planned_progress_is_zero(
    client: TestClient,
    seeded_project,
) -> None:
    response = client.post(
        f"/api/v1/projects/{seeded_project.id}/activities",
        json=_activity_payload(planned_progress=0),
    )
    assert response.status_code == 201
    assert response.json()["evm"]["spi"] is None
