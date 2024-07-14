import pytest
import requests

URL = 'https://jsonplaceholder.typicode.com'


@pytest.mark.parametrize('resource, status_code', [('todos', 200), ('users', 200), ('addresses', 404)])
def test_get_resource(resource, status_code):
    response = requests.get(f'{URL}/{resource}')
    assert response.status_code == status_code


@pytest.mark.parametrize('id, status_code', [(1, 200), ('string', 404), (0, 404)])
def test_get_post_with_id(id, status_code):
    response = requests.get(f'{URL}/posts/{id}')
    assert response.status_code == status_code


def test_create_todo():
    data = {"userId": 10,
            "id": 201,
            "title": "Lorem Ipsum ",
            "completed": "false"
            }
    response = requests.post(f'{URL}/todos', data)
    assert response.status_code == 201


def test_delete_todo(id=201):
    response = requests.delete(f'{URL}/posts/{id}')
    assert response.status_code == 200


@pytest.mark.parametrize('user_id', list(range(1, 10)))
def test_all_users(user_id):
    response = requests.get(f'{URL}/users/{user_id}')
    assert response.status_code == 200
