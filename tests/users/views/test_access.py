
import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.parametrize(
    'data',
    [
        [{
            'email': 'test@example.com',
            'first_name': 'John',
            'last_name': 'Doe',
            'password': 'password123',
        }, status.HTTP_201_CREATED],
        [{
            'first_name': 'John',
            'last_name': 'Doe',
            'password': 'password123',
        }, status.HTTP_400_BAD_REQUEST],
        [{
            'email': 'test@example.com',
            'last_name': 'Doe',
            'password': 'password123',
        }, status.HTTP_400_BAD_REQUEST],
        [{
            'email': 'test@example.com',
            'first_name': 'John',
            'password': 'password123',
        }, status.HTTP_400_BAD_REQUEST],
        [{
            'email': 'test@example.com',
            'first_name': 'John',
            'last_name': 'Doe',
        }, status.HTTP_400_BAD_REQUEST],
    ]
)
def test_access_user_register(data, db, client):
    '''Test of user registration'''
    payload, code = data
    reversed_url = reverse('token_registration')
    response = client.post(reversed_url, data=payload)
    assert response.status_code == code


@pytest.mark.parametrize(
    'data',
    [
        [{
            'email': 'test@example.com',
            'password': 'password123'
        }, status.HTTP_202_ACCEPTED],
        [{
            'password': 'password123'
        }, status.HTTP_400_BAD_REQUEST],
        [{
            'email': 'test@example.com',
        }, status.HTTP_400_BAD_REQUEST],
    ]
)
def test_access_user_login(data, db, client, registered_user):
    '''Test of User authorization'''
    payload, code = data
    reversed_url = reverse('token_obtain_pair')
    response = client.post(reversed_url, data=payload)
    assert response.status_code == code


# @pytest.mark.parametrize(
#     'data',
#     [
#         [{
#             "new_password": "password",
#             "email": "client@user.ru"
#         }, status.HTTP_200_OK],
#         [{
#             'email': 'client@user.ru'
#         }, status.HTTP_400_BAD_REQUEST],
#         [{
#             'new_password': 'password'
#         }, status.HTTP_400_BAD_REQUEST],
#     ]
# )
# def test_access_update_passwords(data, db, user_client):
#     payload, code = data
#     reversed_url = reverse('update_password')
#     headers = {'Content-Type': 'application/json'}
#     payload = json.dumps(payload)
#     response = user_client.patch(reversed_url, data=payload, headers=headers)
#     print(response.json())
#     assert response.status_code == code


@pytest.mark.parametrize(
    'data',
    [
        [None, status.HTTP_200_OK],
        ['123', status.HTTP_401_UNAUTHORIZED],
    ]
)
def test_access_refresh_token(data, db, client, registered_user):
    refresh_code, code = data
    reversed_url = reverse('token_obtain_pair')
    user = registered_user
    data = {
        'email': user.email,
        'password': 'password123'
    }
    response = client.post(reversed_url, data=data)
    refresh = response.json()['refresh']
    reversed_url = reverse('token_refresh')
    if refresh_code is None:
        data = {
            'refresh': refresh
        }
    else:
        data = {
            'refresh': refresh_code
        }
    response = client.post(reversed_url, data=data)
    assert response.status_code == code
