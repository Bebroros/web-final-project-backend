import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_unauthenticated_user(api_client):
    url = reverse('todo-list')
    response = api_client.get(url)
    assert response.status_code == 401


@pytest.mark.django_db
def test_authenticated_user(api_client, user, authenticate):
    url = reverse('todo-list')
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.django_db
def test_get_todo(api_client, user, authenticate, todo):
    url = reverse('todo-detail', args=[todo.pk])
    response = api_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_todo_bad(api_client, user, authenticate, todo):
    url = reverse('todo-detail', args=[999999])
    response = api_client.get(url)
    assert 404 == response.status_code


@pytest.mark.django_db
def test_post_todo(api_client, user, authenticate):
    url = reverse('todo-list')
    response = api_client.post(url, data={'description': 'Test description',
                                          'title': 'Test title',
                                          'importance': 1,
                                          'duration': 30}
                               )
    assert 201 == response.status_code


@pytest.mark.django_db
def test_post_todo_bad(api_client, user, authenticate):
    url = reverse('todo-list')
    response = api_client.post(url, data={'description': 'Test description', })
    assert 400 == response.status_code


@pytest.mark.django_db
def test_patch_todo(api_client, user, authenticate, todo):
    url = reverse('todo-detail', args=[todo.pk])
    response = api_client.patch(url, data={'title': 'New title'})
    assert 200 == response.status_code
    assert response.json()['title'] == 'New title'


@pytest.mark.django_db
def test_patch_todo_unexisting(api_client, user, authenticate, todo):
    url = reverse('todo-detail', args=[999999])
    response = api_client.patch(url, data={'title': 'New title'})
    assert 404 == response.status_code


@pytest.mark.django_db
def test_patch_todo_bad(api_client, user, authenticate, todo):
    url = reverse('todo-detail', args=[todo.pk])
    response = api_client.patch(url, data={'importance': '123abc'})
    assert 400 == response.status_code


@pytest.mark.django_db
def test_delete(api_client, user, authenticate, todo):
    url = reverse('todo-detail', args=[todo.pk])
    response = api_client.delete(url)
    assert 204 == response.status_code


@pytest.mark.django_db
def test_delete_unexisting(api_client, user, authenticate, todo):
    url = reverse('todo-detail', args=[999999])
    response = api_client.delete(url)
    assert 404 == response.status_code
