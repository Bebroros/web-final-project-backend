import pytest


@pytest.mark.django_db
def test_get_token(api_client, user):
    response = api_client.post(
        '/auth/token/',
        {
            'username': user.username,
            'password': "password123",
        }, format='json')
    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_refresh_token(api_client, user):
    token_response = api_client.post(
        '/auth/token/',
        {
            'username': user.username,
            'password': "password123",
        }, format='json')
    token = token_response.data['access']
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    response = api_client.post(
        '/auth/token/refresh/',
        {
            'refresh': token_response.data['refresh'],
        }, format='json'
    )
    assert response.status_code == 200
    assert len(response.data) == 1
