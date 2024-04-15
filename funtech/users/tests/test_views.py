from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APIRequestFactory, APITestCase
from users.models import User
from users.views import UserViewSet
from events.models import Event
from rest_framework.authtoken.models import Token


class UserViewSetTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create(username='test_user')

    def test_get_user(self):
        request = self.factory.get('/api/users/')
        view = UserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user(self):
        request = self.factory.patch(
            '/api/users/', data={'username': 'new_username'}, format='json'
        )
        request.user = self.user
        view = UserViewSet.as_view({'patch': 'partial_update'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'new_username')


class RegisterUserViewTestCase(TestCase):
    def test_register_user_redirect(self):
        client = APIClient()
        response = client.get(reverse('register-user'))
        self.assertEqual(response.status_code, 302)


class CreateTokenAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='test_user', email='test@example.com'
        )

    def test_create_token_success(self):
        code = 'mock_authorization_code'
        request_data = {'code': code}
        response = self.client.get('/api/token/', data=request_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('auth_token', response.data)

    def test_create_token_missing_code(self):
        response = self.client.get('/api/token/')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_invalid_code(self):
        request_data = {'code': 'invalid_code'}
        response = self.client.get('/api/token/', data=request_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class LogoutViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user', password='test_password'
        )
        self.token = Token.objects.create(user=self.user)

    def test_logout_success(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(reverse('logout'))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(Token.objects.filter(key=self.token.key).exists())

    def test_logout_unauthorized(self):
        response = self.client.post(reverse('logout'))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TicketViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='test_user', email='test@example.com'
        )
        self.client.force_authenticate(user=self.user)

    def test_get_tickets(self):
        response = self.client.get('/tickets/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_tickets_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/tickets/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class UserEventViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='test_user', email='test@example.com'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_get_user_data(self):
        response = self.client.get('/api/user-event/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user_event(self):
        event = Event.objects.create(name='Test Event')
        data = {
            'event': event.id,
            'userAgreements': [{'is_signed': True}]
        }
        response = self.client.post('/api/user-event/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_event_missing_data(self):
        response = self.client.post('/api/user-event/')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
