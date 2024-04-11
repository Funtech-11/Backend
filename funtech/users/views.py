import requests
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from users.models import User
from users.serializers import UserSerializer


# events, finished_events -- actions
class UserViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    serializer_class = UserSerializer
    queryset = User.objects.all()  # + prefetch_related 'events'
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class RegisterUser(APIView):
    """User registration API."""

    def get(self, request):
        return redirect('https://oauth.yandex.ru/authorize?response_type=code&client_id=6e05c91a25f74e4c8661025fc46baa2b')


class CreateToken(APIView):
    """Get token API."""

    def get(self, request):
        if request.GET['code']:
            code = request.GET['code']

        res = requests.post(f'https://oauth.yandex.ru/token', data={'grant_type': 'authorization_code',
                                                            'code': code,
                                                            'client_id': '6e05c91a25f74e4c8661025fc46baa2b',
                                                            'client_secret': '25665478fb3644edb43b3246199dd327'})
        #print(res.text)
        if "error" in res:
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
        # Token creation!
        #print(res.json()["access_token"])
        cl = requests.get('https://login.yandex.ru/info?',
                          headers={'Authorization': "Bearer " + res.json()["access_token"]})
        user = cl.json()
        print(user['default_email'])
        User.objects.get_or_create(email=user['default_email'])
        #Token.objects.get_or_create(user=)
        return Response(cl, status=status.HTTP_200_OK)
