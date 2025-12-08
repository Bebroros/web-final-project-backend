import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_unauthenticated_user(api_client):
    url = reverse('get-prediction')
    response = api_client.get(url)
    assert response.status_code == 401


@pytest.mark.django_db
def test_authenticated_user(api_client, authenticate, mocker):
    """using mock server"""
    url = reverse('get-prediction')
    ai_api_url = "https://openrouter.ai/api/v1/chat/completions"

    mocker.post(ai_api_url, json={
        "choices": [{"message": {"content": "Your day will be delightful."}}]
    }, status_code=200)

    response = api_client.get(url)
    assert response.status_code == 200
    assert response.json() == {"horoscope": "Your day will be delightful."}


@pytest.mark.django_db
def test_ai_response_failure(api_client, authenticate, mocker):
    url = reverse('get-prediction')
    ai_api_url = "https://openrouter.ai/api/v1/chat/completions"

    mocker.post(ai_api_url, status_code=500)

    response = api_client.get(url)
    assert response.json() == ({"horoscope": "Stars are not talkative today, but you got this!"})