from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from events.models import Event, Speaker
from events.serializers import EventSerializer, SpeakerSerializer


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

    @extend_schema(
        summary='Посмотреть список мероприятий',
        tags=['Мероприятия'],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary='Создать мероприятие',
        tags=['Мероприятия'],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary='Посмотреть информацию о мероприятии',
        tags=['Мероприятия'],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary='Редактировать мероприятие',
        tags=['Мероприятия'],
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary='Удалить мероприятие',
        tags=['Мероприятия'],
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class SpeakerViewSet(ModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

    @extend_schema(
        summary='Посмотреть список спикеров',
        tags=['Спикеры'],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary='Создать cпикера',
        tags=['Спикеры'],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary='Посмотреть информацию о спикере',
        tags=['Спикеры'],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary='Редактировать спикера',
        tags=['Спикеры'],
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary='Удалить спикера',
        tags=['Спикеры'],
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
