import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_unauthenticated_user(api_client):
    url = reverse('sub-list')
    response = api_client.get(url)
    assert response.status_code == 401


@pytest.mark.django_db
def test_authenticated_user(api_client, user, authenticate):
    url = reverse('sub-list')
    response = api_client.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.django_db
def test_get_sub(api_client, user, authenticate, sub):
    url = reverse('sub-detail', args=[sub.pk])
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.json()['name'] == sub.name


@pytest.mark.django_db
def test_bad_sub(api_client, user, authenticate):
    url = reverse('sub-detail', args=[999999])
    response = api_client.get(url)
    assert response.status_code == 404


@pytest.mark.django_db
def test_post_sub(api_client, user, authenticate):
    url = reverse('sub-list')
    payload = {
        "name": "Spotify",
        "payment_date": "2024-02-01",
        "cost": "5.99",
        "cycle": "monthly"
    }
    response = api_client.post(url, payload, format="json")

    assert response.status_code == 201
    assert response.json()['name'] == 'Spotify'
    assert response.json()['cost'] == '5.99'


@pytest.mark.django_db
def test_bad_post_sub(api_client, user, authenticate):
    url = reverse('sub-list')
    response = api_client.post(url, {"name": "Incomplete Sub"}, format="json")

    assert response.status_code == 400


@pytest.mark.django_db
def test_patch_sub(api_client, user, authenticate, sub):
    url = reverse('sub-detail', args=[sub.pk])
    response = api_client.patch(url, {"cost": "20.50"}, format="json")

    assert response.status_code == 200
    assert response.json()["cost"] == "20.50"


@pytest.mark.django_db
def test_patch_unexisting_sub(api_client, user, authenticate):
    url = reverse('sub-detail', args=[999999])
    response = api_client.patch(url, {"name": "New Name"}, format="json")

    assert response.status_code == 404


@pytest.mark.django_db
def test_bad_patch_sub(api_client, user, authenticate, sub):
    url = reverse('sub-detail', args=[sub.id])
    response = api_client.patch(url, {"cost": "not-a-number"}, format="json")

    assert response.status_code == 400


@pytest.mark.django_db
def test_delete_sub(api_client, user, authenticate, sub):
    url = reverse('sub-detail', args=[sub.pk])
    response = api_client.delete(url)
    assert response.status_code == 204


@pytest.mark.django_db
def test_unexisting_delete_sub(api_client, user, authenticate):
    url = reverse('sub-detail', args=[999999])
    response = api_client.delete(url)
    assert response.status_code == 404
