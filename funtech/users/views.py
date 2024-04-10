from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)

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
    UserExpertiseSerializer
)


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


