from fastapi.testclient import TestClient


def test_create_project_successfully(client: TestClient) -> None:
    payload = {"name": "Proyecto API", "description": "CRUD de proyectos"}

    response = client.post("/api/v1/projects", json=payload)

    assert response.status_code == 201
    body = response.json()
    assert body["id"]
    assert body["name"] == payload["name"]
    assert body["description"] == payload["description"]
    assert body["created_at"]
    assert body["updated_at"]


def test_list_projects_successfully(client: TestClient, seeded_project) -> None:
    response = client.get("/api/v1/projects")

    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, list)
    assert len(body) == 1
    assert body[0]["id"] == str(seeded_project.id)
    assert body[0]["name"] == seeded_project.name
    assert body[0]["description"] == seeded_project.description


def test_get_project_by_id_successfully(client: TestClient, seeded_project) -> None:
    response = client.get(f"/api/v1/projects/{seeded_project.id}")

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == str(seeded_project.id)
    assert body["name"] == seeded_project.name
    assert body["description"] == seeded_project.description
    assert body["created_at"]
    assert body["updated_at"]


def test_return_404_when_project_does_not_exist(client: TestClient) -> None:
    response = client.get("/api/v1/projects/11111111-1111-1111-1111-111111111111")

    assert response.status_code == 404
    assert response.json() == {"detail": "Project not found"}


def test_update_project_successfully(client: TestClient, seeded_project) -> None:
    payload = {"name": "Proyecto actualizado", "description": "Descripcion nueva"}

    response = client.put(f"/api/v1/projects/{seeded_project.id}", json=payload)

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == str(seeded_project.id)
    assert body["name"] == payload["name"]
    assert body["description"] == payload["description"]


def test_delete_project_successfully(client: TestClient, seeded_project) -> None:
    response = client.delete(f"/api/v1/projects/{seeded_project.id}")

    assert response.status_code == 204
    assert response.text == ""

    fetch_response = client.get(f"/api/v1/projects/{seeded_project.id}")
    assert fetch_response.status_code == 404


def test_validate_project_name_is_required(client: TestClient) -> None:
    response = client.post("/api/v1/projects", json={"description": "Sin nombre"})
    assert response.status_code == 422

    response_empty = client.post(
        "/api/v1/projects",
        json={"name": "   ", "description": "Nombre invalido"},
    )
    assert response_empty.status_code == 422
