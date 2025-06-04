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
    assert response.json() == {'hello': 'world'}
    assert response.status_code == HTTPStatus.OK
