from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from events.models import Event, Speaker, Location


class EventViewSetTestCase(APITestCase):
    def setUp(self):
        self.event_data = {
            'name': 'Мероприятие 1',
            'date_time_start': '2024-04-15T10:00:00',
            'date_time_end': '2024-04-15T18:00:00',
            'max_participants': 100,
            'information': 'Описание мероприятия',
            'event_type': 'Тип мероприятия',
            'event_format': 'Формат мероприятия',
            'activity_status': 'Активное',
            'video': 'video.mp4'
        }
        self.event = Event.objects.create(**self.event_data)
        self.url = reverse('event-list')

    def test_get_event_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_event(self):
        response = self.client.post(self.url, self.event_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        event = Event.objects.get(name='Мероприятие 1')
        self.assertIsNotNone(event)

    def test_retrieve_event(self):
        url = reverse('event-detail', kwargs={'pk': self.event.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_event(self):
        url = reverse('event-detail', kwargs={'pk': self.event.pk})
        updated_data = {'name': 'Новое мероприятие'}
        response = self.client.patch(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.event.refresh_from_db()
        self.assertEqual(self.event.name, 'Новое мероприятие')

    def test_delete_event(self):
        url = reverse('event-detail', kwargs={'pk': self.event.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Event.objects.filter(pk=self.event.pk).exists())


class SpeakerViewSetTestCase(APITestCase):
    def setUp(self):
        self.speaker_data = {
            'name': 'Имя Спикера',
            'job': 'Должность',
        }
        self.speaker = Speaker.objects.create(**self.speaker_data)
        self.url = reverse('speaker-list')

    def test_get_speaker_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_speaker(self):
        url = reverse('speaker-detail', kwargs={'pk': self.speaker.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_speaker(self):
        url = reverse('speaker-detail', kwargs={'pk': self.speaker.pk})
        updated_data = {'name': 'Новое имя'}
        response = self.client.patch(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.speaker.refresh_from_db()
        self.assertEqual(self.speaker.name, 'Новое имя')

    def test_delete_speaker(self):
        url = reverse('speaker-detail', kwargs={'pk': self.speaker.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Speaker.objects.filter(pk=self.speaker.pk).exists())


class LocationViewSetTestCase(APITestCase):
    def setUp(self):
        self.location_data = {
            'city': 'Город',
            'address': 'Адрес',
            'builing': 'Здание',
            'metro_station': 'Станция метро',
        }
        self.location = Location.objects.create(**self.location_data)
        self.url = reverse('location-list')

    def test_get_location_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_location(self):
        url = reverse('location-detail', kwargs={'pk': self.location.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_location(self):
        url = reverse('location-detail', kwargs={'pk': self.location.pk})
        updated_data = {'city': 'Новый город'}
        response = self.client.patch(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.location.refresh_from_db()
        self.assertEqual(self.location.city, 'Новый город')

    def test_delete_location(self):
        url = reverse('location-detail', kwargs={'pk': self.location.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Location.objects.filter(pk=self.location.pk).exists())
