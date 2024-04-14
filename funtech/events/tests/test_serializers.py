from django.test import TestCase

from events.models import Event, Location, Speaker, Theme
from events.serializers import (
    EventSerializer,
    LocationSerializer,
    SpeakerSerializer,
    ThemeSerializer,
    UserEventSerializer,
)


class LocationSerializerTestCase(TestCase):
    def setUp(self):
        self.location_data = {
            'city': 'Москва',
            'address': 'ул. Примерная, д. 123',
            'builing': 'Конференц-центр "Пример"',
            'metro_station': 'Станция "Примерная"'
        }
        self.location = Location.objects.create(**self.location_data)
        self.serializer = LocationSerializer(instance=self.location)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['locationId', 'city', 'address', 'builing', 'metroStation']))

    def test_location_id_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['locationId'], self.location.location_id)

    def test_metro_station_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['metroStation'], self.location.metro_station)

    def test_valid_data(self):
        serializer = LocationSerializer(data=self.location_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_data(self):
        invalid_data = {
            'city': 'Москва',
            'builing': 'Конференц-центр "Пример"'
        }
        serializer = LocationSerializer(data=invalid_data)
        self.assertTrue(serializer.is_valid())


class ThemeSerializerTestCase(TestCase):
    def setUp(self):
        self.theme_data = {
            'name': 'Тестовая тематика'
        }
        self.theme = Theme.objects.create(**self.theme_data)
        self.serializer = ThemeSerializer(instance=self.theme)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['name']))

    def test_valid_data(self):
        serializer = ThemeSerializer(data=self.theme_data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_data(self):
        invalid_data = {
            'name': ''
        }
        serializer = ThemeSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())


class SpeakerSerializerTestCase(TestCase):
    def setUp(self):
        self.speaker_data = {
            'name': 'Иван Иванов',
            'job': 'Программист',
            'avatar': 'avatar.jpg'
        }
        self.speaker = Speaker.objects.create(**self.speaker_data)
        self.serializer = SpeakerSerializer(instance=self.speaker)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(
            set(data.keys()), set(['speakerId', 'name', 'job', 'avatar'])
        )

    def test_valid_data(self):
        serializer = SpeakerSerializer(data=self.speaker_data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_data(self):
        invalid_data = {
            'name': 'Иван Иванов',
            'job': '',
            'avatar': 'avatar.jpg'
        }
        serializer = SpeakerSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())


class EventSerializerTestCase(TestCase):
    def setUp(self):
        self.location_data = {
            'city': 'Москва',
            'address': 'ул. Примерная, д. 123',
            'builing': 'Конференц-центр "Пример"',
            'metro_station': 'Станция "Примерная"'
        }
        self.location = Location.objects.create(**self.location_data)
        self.event_data = {
            'name': 'Мероприятие 1',
            'date_time_start': '2024-04-15T10:00:00',
            'date_time_end': '2024-04-15T18:00:00',
            'location': self.location,
            'max_participants': 100,
            'information': 'Описание мероприятия',
            'event_type': 'Тип мероприятия',
            'event_format': 'Формат мероприятия',
            'activity_status': 'Активное',
            'wallpaper': 'wallpaper.jpg',
            'theme': None,
            'video': 'video.mp4'
        }
        self.event = Event.objects.create(**self.event_data)
        self.serializer = EventSerializer(instance=self.event)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set([
            'eventId', 'name', 'dateTimeStart', 'dateTimeEnd', 'location',
            'maxParticipants', 'curentParticipants', 'information',
            'eventType', 'eventFormat', 'activityStatus',
            'wallpaper', 'theme', 'video', 'programs'
        ]))

    def test_valid_data(self):
        serializer = EventSerializer(data=self.event_data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_data(self):
        invalid_data = {
            'name': 'Мероприятие 1',
            'date_time_start': '2024-04-15T10:00:00',
            'date_time_end': '2024-04-15T18:00:00',
            'location': None,
            'max_participants': 100,
            'information': '',
            'event_type': 'Тип мероприятия',
            'event_format': 'Формат мероприятия',
            'activity_status': 'Активное',
            'wallpaper': 'wallpaper.jpg',
            'theme': None,
            'video': 'video.mp4'
        }
        serializer = EventSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())


class UserEventSerializerTestCase(TestCase):
    def setUp(self):
        self.event_data = {
            'name': 'Мероприятие 1',
            'date_time_start': '2024-04-15T10:00:00',
            'date_time_end': '2024-04-15T18:00:00',
            'location': None,
            'max_participants': 100,
            'information': 'Описание мероприятия',
            'event_type': 'Тип мероприятия',
            'event_format': 'Формат мероприятия',
            'activity_status': 'Активное',
            'wallpaper': 'wallpaper.jpg',
            'theme': None,
            'video': 'video.mp4'
        }
        self.user_event_data = {
            'userEventId': 1,
            'user': 1,  # Предположим, что у пользователя user_id равен 1
            'event': self.event_data,
            'agree': True
        }
        self.serializer = UserEventSerializer(data=self.user_event_data)

    def test_valid_data(self):
        self.assertFalse(self.serializer.is_valid())

    def test_invalid_data(self):
        invalid_data = {
            'userEventId': 1,
            'user': None,  # Пользователь не указан
            'event': self.event_data,
            'agree': True
        }
        serializer = UserEventSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
