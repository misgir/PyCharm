import requests
import pytest


BASE_URL = "https://ru.yougile.com/api-v2"

PROJECT_DATA = {
    'name': 'Test Project',
    'description': 'This is a test project.'
}

INVALID_PROJECT_DATA = {
    'name': '',
    'description': 'This should fail due to missing name.'
}

HEADERS = {
    #'Authorization': 'Bearer ', # Раскомментируйте и добавьте ваш токен
    'Content-Type': 'application/json'
}

def test_create_project():
    response = requests.post(f"{BASE_URL}/projects", json=PROJECT_DATA, headers=HEADERS)
    assert response.status_code == 20
    assert "id" in response.json()
def test_get_projects():
    response = requests.get(f"{BASE_URL}/projects", headers=HEADERS)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_project():
    project_id = 1  # Замените на актуальный ID проекта для тестирования
    update_data = {
        "name": "Updated Project",
        "description": "This project has been updated."
    }
    response = requests.put(f"{BASE_URL}/projects/{project_id}", json=update_data, headers=HEADERS)
    assert response.status_code == 200
    assert response.json()['name'] == "Updated Project"

def test_get_specific_project():
    project_id = 1  # Замените на актуальный ID проекта для тестирования
    response = requests.get(f"{BASE_URL}/projects/{project_id}", headers=HEADERS)
    assert response.status_code == 200
    assert response.json()['id'] == project_id

def test_create_project_missing_name():
    response = requests.post(f"{BASE_URL}/projects", json=INVALID_PROJECT_DATA, headers=HEADERS)
    assert response.status_code == 400
    assert "name" in response.json()['errors']
