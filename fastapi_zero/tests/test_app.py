from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root():
    """
    Etapa teste triplo (AAA):
    - A: Arrange - Arranjo
    - A: Act - Ação
    - A: Assert - Afirmação
    """

    # Arrange
    client = TestClient(app)

    # Act
    response = client.get('/')

    # Assert
    assert response.json() == {'message': 'hello world'}
    assert response.status_code == HTTPStatus.OK


def test_page_html():
    client = TestClient(app)

    reponse = client.get('/page')

    assert reponse.status_code == HTTPStatus.OK
    assert '<h1> hello world </h1>' in reponse.text


def test_create_user():
    client = TestClient(app)

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
