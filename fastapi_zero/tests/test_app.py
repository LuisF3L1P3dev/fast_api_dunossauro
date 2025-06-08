from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from fastapi_zero.app import app


@pytest.fixture
def client():
    return TestClient(app)


def test_root(client):
    """
    Etapa teste triplo (AAA):
    - A: Arrange - Arranjo
    - A: Act - Ação
    - A: Assert - Afirmação
    """

    # Arrange já está no pytest

    # Act
    response = client.get('/')

    # Assert
    assert response.json() == {'message': 'hello world'}
    assert response.status_code == HTTPStatus.OK


def test_page_html(client):
    reponse = client.get('/page')

    assert reponse.status_code == HTTPStatus.OK
    assert '<h1> hello world </h1>' in reponse.text


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'alice',
        'email': 'alice@example.com',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'alice',
                'email': 'alice@example.com',
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'bob',
        'email': 'bob@example.com',
    }
