from django.urls import path
from rest_framework import routers

from .views import CreateToken, RegisterUser, UserViewSet

router = routers.DefaultRouter()
# router.register(r'me', UserViewSet, basename='user')

urlpatterns = [
    path('me', UserViewSet.as_view({'get': 'retrieve'})),
    path('reg/', RegisterUser.as_view()),
    path('token/', CreateToken.as_view()),
]
