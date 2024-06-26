# import requests
# from django.shortcuts import redirect
from events.models import Event, UserEvent
from rest_framework import status, viewsets
# from rest_framework.authtoken.models import Token
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import TicketSerializer, UserSerializer


AUTH_URL = 'https://oauth.yandex.ru/'


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


# class RegisterUser(APIView):
#     """User registration API."""

    # def get(self, request):
    #     return redirect(
    #         f'{AUTH_URL}authorize?response_type=code&client_id={CLIENT_ID}'
    #     )


# class CreateToken(APIView):
#     """Get token API."""

#     def get(self, request):
#         if request.GET['code']:
#             code = request.GET['code']

#         res = requests.post(
#             'https://oauth.yandex.ru/token',
#             data={
#                 'grant_type': 'authorization_code',
#                 'code': code,
#                 'client_id': '6e05c91a25f74e4c8661025fc46baa2b',
#                 'client_secret': '25665478fb3644edb43b3246199dd327'
#             }
#         )
#         if "error" in res:
#             return Response(res, status=status.HTTP_400_BAD_REQUEST)
#         # Token creation!
#         cl = requests.get('https://login.yandex.ru/info?',
#                           headers={'Authorization': "Bearer " +
#                                    res.json()["access_token"]})
#         user = cl.json()
#         print(user)
#         user, _ = User.objects.get_or_create(email=user['default_email'],
#                                              username=user['login'])
#         print(user)
#         try:
#             token = Token.objects.get(user=user)
#             token.delete()
#             token = Token.objects.create(user=user)
#         except Token.DoesNotExist:
#             token = Token.objects.create(user=user)
#         return Response({'auth_token': str(token)},
#                         status=status.HTTP_200_OK)


# class LogoutView(APIView):
#     """Представление выхода пользователя."""
#     def post(self, request):
#         Token.objects.get(key=request.auth).delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class TicketView(ListAPIView):
    serializer_class = TicketSerializer

    def get_queryset(self):
        qs = UserEvent.objects.filter(user=self.request.user)
        return qs


class UserEventView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        user = User.objects.get(pk=request.user.pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        user = User.objects.get(pk=request.user.pk)
        print(request.data)
        event_id = request.data.pop('eventId')
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        event = Event.objects.get(pk=event_id)
        agree = request.data['userAgreements'][0]['isSigned']
        try:
            us = UserEvent.objects.get(user=user, event=event, agree=agree)
            us.delete()
            UserEvent.objects.create(user=user, event=event, agree=agree)
        except UserEvent.DoesNotExist:
            UserEvent.objects.create(user=user, event=event, agree=agree)

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
