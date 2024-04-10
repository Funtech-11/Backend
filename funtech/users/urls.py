from django.urls import path
from rest_framework import routers

from .views import UserViewSet

router = routers.DefaultRouter()
# router.register(r'me', UserViewSet, basename='user')

urlpatterns = [
    path('me', UserViewSet.as_view({'get': 'retrieve'}))
]
