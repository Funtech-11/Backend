from rest_framework.decorators import action
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, permissions, status, filters
from rest_framework.authtoken.models import Token
from users.permissions import OwnerOrReadOnly
import requests
from rest_framework.response import Response

from .models import (
    User,
    Agreement,
    UserAgreement,
    Expertise,
    Stack,
    UserExpertise
)
from .serializers import (
    UserSerializer,
    AgreementSerializer,
    UserAgreementSerializer,
    ExpertiseSerializer,
    StackSerializer,
    UserExpertiseSerializer,
    UserEventSerializer
)


# events, finished_events -- actions
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()  # + prefetch_related 'events'
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'patch']

    def get_object(self):
        return self.request.user
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class RegisterUser(APIView):
    """User registration API."""

    def get(self, request):
        return redirect('https://oauth.yandex.ru/authorize?response_type=code&client_id=6e05c91a25f74e4c8661025fc46baa2b')


class CreateToken(APIView):
    """Get token API."""

    def get(self, request):
        if request.GET['code']:
            code = request.GET['code']

        res = requests.post('https://oauth.yandex.ru/token', data={'grant_type': 'authorization_code',
                                                            'code': code,
                                                            'client_id': '6e05c91a25f74e4c8661025fc46baa2b',
                                                            'client_secret': '25665478fb3644edb43b3246199dd327'})
        if "error" in res:
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
        # Token creation!
        cl = requests.get('https://login.yandex.ru/info?',
                          headers={'Authorization': "Bearer " +
                                   res.json()["access_token"]})
        user = cl.json()
        print(user)
        user, _ = User.objects.get_or_create(email=user['default_email'],
                                             username=user['login'])
        print(user)
        try:
            token = Token.objects.get(user=user)
            token.delete()
            token = Token.objects.create(user=user)
        except Token.DoesNotExist:
            token = Token.objects.create(user=user)
        return Response({'auth_token': str(token)},
                        status=status.HTTP_200_OK)


class LogoutView(APIView):
    """Представление выхода пользователя."""
    def post(self, request):
        Token.objects.get(key=request.auth).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserEventView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        user = User.objects.get(pk=request.user.pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):

        user = User.objects.get(pk=request.user.pk)
        serializer = UserEventSerializer(event_id=pk,
                                         data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



# class UserDetailView(APIView):

#     permission_classes = (OwnerOrReadOnly,)

#     def get(self, request, pk):
#         try:
#             user = User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = UserSerializer(user)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request, pk):
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)


