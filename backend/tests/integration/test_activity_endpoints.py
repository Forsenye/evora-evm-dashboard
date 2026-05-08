from fastapi.testclient import TestClient


def test_get_project_activities(client: TestClient, seeded_project) -> None:
    response = client.get(f'/projects/{seeded_project.id}/activities')
    assert response.status_code == 200
    assert response.json() == []


def test_get_project_activities_project_not_found(client: TestClient) -> None:
    response = client.get('/projects/11111111-1111-1111-1111-111111111111/activities')
    assert response.status_code == 404
    assert response.json()['detail'] == 'Project not found'
