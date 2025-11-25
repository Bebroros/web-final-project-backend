import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_unauthenticated_user(api_client):
    url = reverse('event-list')
    response = api_client.get(url)
    assert response.status_code == 401


@pytest.mark.django_db
def test_authenticated_user(api_client, user, authenticate):
    url = reverse('event-list')
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.django_db
def test_get_event(api_client, user, authenticate, event):
    url = reverse('event-detail', args=[event.pk])
    response = api_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_bad_event(api_client, user, authenticate, event):
    url = reverse('event-detail', args=[999999])
    response = api_client.get(url)
    assert response.status_code == 404


@pytest.mark.django_db
def test_post_event(api_client, user, authenticate):
    url = reverse('event-list')
    response = api_client.post(url, {"title": "test",
                                     "description": "test",
                                     "importance": 1,
                                     "start_at":  "2000-01-01",
                                     "end_at": "2000-01-01",
                                     }, format="json")
    assert response.status_code == 201
    assert response.json()['title'] == 'test'
    assert response.json()['description'] == 'test'


@pytest.mark.django_db
def test_bad_post_event(api_client, user, authenticate):
    url = reverse('event-list')
    response = api_client.post(url, {"title": "test"}, format="json")

    assert response.status_code == 400


@pytest.mark.django_db
def test_patch_event(api_client, user, authenticate, event):
    url = reverse('event-detail', args=[event.pk])
    response = api_client.patch(url, {"title": "new_title"}, format="json")
    assert response.status_code == 200
    assert response.json()["title"] == "new_title"


@pytest.mark.django_db
def test_patch_unexisting_event(api_client, user, authenticate):
    url = reverse('event-detail', args=[999999])
    response = api_client.patch(url, {"title": "new_title"}, format="json")

    assert response.status_code == 404


@pytest.mark.django_db
def test_bad_patch_event(api_client, user, authenticate, event):
    url = reverse('event-detail', args=[event.id])
    response = api_client.patch(url, {"importance": "1234kji"}, format="json")
    assert response.status_code == 400


@pytest.mark.django_db
def test_delete_event(api_client, user, authenticate, event):
    url = reverse('event-detail', args=[event.pk])
    response = api_client.delete(url)
    assert response.status_code == 204


@pytest.mark.django_db
def test_unexisting_delete_event(api_client, user, authenticate):
    url = reverse('event-detail', args=[999999])
    response = api_client.delete(url)
    assert response.status_code == 404
