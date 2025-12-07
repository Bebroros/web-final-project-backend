import pytest
import requests_mock
from rest_framework.test import APIClient
from events.models import Event
from subscriptions.models import Subs
from user_auth.models import CustomUser
from todo.models import Todo


@pytest.fixture(scope='function')
def api_client():
    return APIClient()


@pytest.fixture(scope='function')
def user():
    user = CustomUser.objects.create_user(username='testuser',
                                          password='password123',
                                          email='test@test.test',
                                          first_name='test',
                                          last_name='test',
                                          date="2000-1-1"
                                          )
    return user


@pytest.fixture(scope='function')
def authenticate(api_client, user):
    response = api_client.post(
        '/auth/token/',
        {
            'username': user.username,
            'password': "password123",
        }, format='json')
    assert response.status_code == 200
    token = response.data['access']
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    yield token


@pytest.fixture(scope='function')
def event(user, authenticate):
    event = Event.objects.create(title="Test event",
                                 description="Test description",
                                 importance=1,
                                 start_at="2025-1-1",
                                 end_at="2025-2-1",
                                 notified=False,
                                 owner=user)
    return event


@pytest.fixture(scope='function')
def sub(user):
    return Subs.objects.create(
        owner=user,
        name="Netflix Premium",
        payment_date="2024-01-01",
        cost="15.99",
        cycle="monthly"
    )


@pytest.fixture(scope='function')
def todo(user):
    return Todo.objects.create(
        owner=user,
        title='TestTodo',
        importance=1,
        duration=30,
        description='Test description',
    )

@pytest.fixture(scope='function')
def mocker():
    with requests_mock.Mocker() as mock:
        yield mock