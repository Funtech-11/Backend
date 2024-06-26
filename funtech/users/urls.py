from django.urls import path
from rest_framework import routers

from users.views import (
    # CreateToken,
    # RegisterUser,
    TicketView,
    UserEventView,
    UserViewSet,
)

router = routers.DefaultRouter()
# router.register(r'me', UserViewSet, basename='user')

urlpatterns = [
    path('me/', UserViewSet.as_view({'get': 'retrieve',
                                     'patch': 'partial_update'})),
    path('me/tickets/', TicketView.as_view()),
    # path('reg/', RegisterUser.as_view()),
    # path('token/', CreateToken.as_view()),
    path('events/', UserEventView.as_view()),
]
