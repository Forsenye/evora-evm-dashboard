from fastapi.testclient import TestClient


def test_get_health(client: TestClient) -> None:
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json() == {'status': 'ok', 'service': 'EVORA API'}


def test_get_projects(client: TestClient) -> None:
    response = client.get('/projects')
    assert response.status_code == 200
    assert response.json() == []


def test_get_project_by_id(client: TestClient, seeded_project) -> None:
    response = client.get(f'/projects/{seeded_project.id}')
    assert response.status_code == 200
    payload = response.json()
    assert payload['id'] == str(seeded_project.id)
    assert payload['name'] == seeded_project.name


def test_get_project_by_id_not_found(client: TestClient) -> None:
    response = client.get('/projects/11111111-1111-1111-1111-111111111111')
    assert response.status_code == 404
    assert response.json()['detail'] == 'Project not found'
