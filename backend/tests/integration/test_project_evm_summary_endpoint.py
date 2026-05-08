import pytest
from fastapi.testclient import TestClient


def _create_activity(
    client: TestClient,
    project_id: str,
    *,
    name: str,
    bac: float,
    planned_progress: float,
    actual_progress: float,
    actual_cost: float,
) -> dict:
    payload = {
        "name": name,
        "bac": bac,
        "planned_progress": planned_progress,
        "actual_progress": actual_progress,
        "actual_cost": actual_cost,
    }
    response = client.post(f"/api/v1/projects/{project_id}/activities", json=payload)
    assert response.status_code == 201
    return response.json()


def _seed_reference_activities(client: TestClient, project_id: str) -> None:
    _create_activity(
        client,
        project_id,
        name="Diseno de base de datos",
        bac=1_000_000,
        planned_progress=50,
        actual_progress=40,
        actual_cost=600_000,
    )
    _create_activity(
        client,
        project_id,
        name="Desarrollo backend",
        bac=1_000_000,
        planned_progress=60,
        actual_progress=60,
        actual_cost=700_000,
    )
    _create_activity(
        client,
        project_id,
        name="Integracion frontend",
        bac=1_000_000,
        planned_progress=40,
        actual_progress=20,
        actual_cost=400_000,
    )


def test_get_project_evm_summary_successfully(client: TestClient, seeded_project) -> None:
    _seed_reference_activities(client, str(seeded_project.id))

    response = client.get(f"/api/v1/projects/{seeded_project.id}/evm-summary")

    assert response.status_code == 200
    body = response.json()
    assert body["project_id"] == str(seeded_project.id)
    assert body["project_name"] == seeded_project.name
    assert body["total_activities"] == 3
    assert isinstance(body["activities"], list)


def test_return_404_when_project_does_not_exist(client: TestClient) -> None:
    response = client.get("/api/v1/projects/11111111-1111-1111-1111-111111111111/evm-summary")

    assert response.status_code == 404
    assert response.json() == {"detail": "Project not found"}


def test_return_controlled_summary_when_project_has_no_activities(
    client: TestClient, seeded_project
) -> None:
    response = client.get(f"/api/v1/projects/{seeded_project.id}/evm-summary")

    assert response.status_code == 200
    body = response.json()
    assert body["total_activities"] == 0
    assert body["activities"] == []
    assert body["status"] == "Sin actividades registradas"
    assert body["summary"] == {
        "bac": 0.0,
        "pv": 0.0,
        "ev": 0.0,
        "ac": 0.0,
        "cv": 0.0,
        "sv": 0.0,
        "cpi": None,
        "spi": None,
        "eac": None,
        "vac": None,
        "cost_status": "No calculable",
        "schedule_status": "No calculable",
    }


def test_calculate_total_bac_correctly(client: TestClient, seeded_project) -> None:
    _seed_reference_activities(client, str(seeded_project.id))
    response = client.get(f"/api/v1/projects/{seeded_project.id}/evm-summary")
    assert response.status_code == 200
    assert response.json()["summary"]["bac"] == 3_000_000


def test_calculate_total_pv_correctly(client: TestClient, seeded_project) -> None:
    _seed_reference_activities(client, str(seeded_project.id))
    response = client.get(f"/api/v1/projects/{seeded_project.id}/evm-summary")
    assert response.status_code == 200
    assert response.json()["summary"]["pv"] == 1_500_000


def test_calculate_total_ev_correctly(client: TestClient, seeded_project) -> None:
    _seed_reference_activities(client, str(seeded_project.id))
    response = client.get(f"/api/v1/projects/{seeded_project.id}/evm-summary")
    assert response.status_code == 200
    assert response.json()["summary"]["ev"] == 1_200_000


def test_calculate_total_ac_correctly(client: TestClient, seeded_project) -> None:
    _seed_reference_activities(client, str(seeded_project.id))
    response = client.get(f"/api/v1/projects/{seeded_project.id}/evm-summary")
    assert response.status_code == 200
    assert response.json()["summary"]["ac"] == 1_700_000


def test_calculate_consolidated_cv_correctly(client: TestClient, seeded_project) -> None:
    _seed_reference_activities(client, str(seeded_project.id))
    response = client.get(f"/api/v1/projects/{seeded_project.id}/evm-summary")
    assert response.status_code == 200
    assert response.json()["summary"]["cv"] == -500_000


def test_calculate_consolidated_sv_correctly(client: TestClient, seeded_project) -> None:
    _seed_reference_activities(client, str(seeded_project.id))
    response = client.get(f"/api/v1/projects/{seeded_project.id}/evm-summary")
    assert response.status_code == 200
    assert response.json()["summary"]["sv"] == -300_000


def test_calculate_consolidated_cpi_correctly_from_totals(
    client: TestClient, seeded_project
) -> None:
    _seed_reference_activities(client, str(seeded_project.id))
    response = client.get(f"/api/v1/projects/{seeded_project.id}/evm-summary")
    assert response.status_code == 200
    assert response.json()["summary"]["cpi"] == pytest.approx(0.71, rel=1e-3)


def test_calculate_consolidated_spi_correctly_from_totals(
    client: TestClient, seeded_project
) -> None:
    _seed_reference_activities(client, str(seeded_project.id))
    response = client.get(f"/api/v1/projects/{seeded_project.id}/evm-summary")
    assert response.status_code == 200
    assert response.json()["summary"]["spi"] == pytest.approx(0.8, rel=1e-3)


def test_verify_consolidated_cpi_spi_are_not_calculated_as_averages(
    client: TestClient,
    seeded_project,
) -> None:
    _seed_reference_activities(client, str(seeded_project.id))
    response = client.get(f"/api/v1/projects/{seeded_project.id}/evm-summary")
    assert response.status_code == 200

    body = response.json()
    activity_cpies = [
        row["evm"]["cpi"] for row in body["activities"] if row["evm"]["cpi"] is not None
    ]
    activity_spies = [
        row["evm"]["spi"] for row in body["activities"] if row["evm"]["spi"] is not None
    ]
    avg_cpi = sum(activity_cpies) / len(activity_cpies)
    avg_spi = sum(activity_spies) / len(activity_spies)

    assert body["summary"]["cpi"] != pytest.approx(avg_cpi, rel=1e-3)
    assert body["summary"]["spi"] != pytest.approx(avg_spi, rel=1e-3)


def test_return_cpi_none_when_total_ac_is_zero(client: TestClient, seeded_project) -> None:
    _create_activity(
        client,
        str(seeded_project.id),
        name="Actividad sin AC",
        bac=1_000_000,
        planned_progress=60,
        actual_progress=50,
        actual_cost=0,
    )

    response = client.get(f"/api/v1/projects/{seeded_project.id}/evm-summary")
    assert response.status_code == 200
    body = response.json()
    assert body["summary"]["ac"] == 0
    assert body["summary"]["cpi"] is None
    assert body["summary"]["eac"] is None
    assert body["summary"]["vac"] is None


def test_return_spi_none_when_total_pv_is_zero(client: TestClient, seeded_project) -> None:
    _create_activity(
        client,
        str(seeded_project.id),
        name="Actividad sin PV",
        bac=1_000_000,
        planned_progress=0,
        actual_progress=50,
        actual_cost=250_000,
    )

    response = client.get(f"/api/v1/projects/{seeded_project.id}/evm-summary")
    assert response.status_code == 200
    body = response.json()
    assert body["summary"]["pv"] == 0
    assert body["summary"]["spi"] is None


def test_include_activities_with_individual_evm_indicators(
    client: TestClient,
    seeded_project,
) -> None:
    _seed_reference_activities(client, str(seeded_project.id))

    response = client.get(f"/api/v1/projects/{seeded_project.id}/evm-summary")
    assert response.status_code == 200
    body = response.json()
    first = body["activities"][0]

    assert first["name"] == "Diseno de base de datos"
    assert first["bac"] == 1_000_000
    assert first["planned_progress"] == 50
    assert first["actual_progress"] == 40
    assert first["actual_cost"] == 600_000
    assert first["evm"] == {
        "bac": 1_000_000.0,
        "pv": 500_000.0,
        "ev": 400_000.0,
        "ac": 600_000.0,
        "cv": -200_000.0,
        "sv": -100_000.0,
        "cpi": 0.67,
        "spi": 0.8,
        "eac": 1_500_000.0,
        "vac": -500_000.0,
        "cost_status": "Sobre presupuesto",
        "schedule_status": "Atrasado",
    }


def test_validate_response_contract_for_dashboard(client: TestClient, seeded_project) -> None:
    _seed_reference_activities(client, str(seeded_project.id))

    response = client.get(f"/api/v1/projects/{seeded_project.id}/evm-summary")
    assert response.status_code == 200
    body = response.json()

    assert set(body.keys()) == {
        "project_id",
        "project_name",
        "total_activities",
        "summary",
        "activities",
        "status",
    }

    assert set(body["summary"].keys()) == {
        "bac",
        "pv",
        "ev",
        "ac",
        "cv",
        "sv",
        "cpi",
        "spi",
        "eac",
        "vac",
        "cost_status",
        "schedule_status",
    }

    assert isinstance(body["activities"], list)
    assert len(body["activities"]) == 3
