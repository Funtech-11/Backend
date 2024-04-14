from django.test import TestCase

from events.models import (
    Event,
    Location,
    Photo,
    Program,
    Speaker,
    Theme,
    UserEvent
)
from datetime import datetime
from django.utils import timezone
from users.models import User


class LocationModelTestCase(TestCase):
    def setUp(self):
        self.location = Location.objects.create(
            city='Москва',
            address='ул. Примерная, д. 123',
            builing='Конференц-центр "Пример"',
            metro_station='Станция "Примерная"'
        )

    def test_model_creation(self):
        self.assertIsNotNone(self.location)

    def test_model_update(self):
        self.location.city = 'Санкт-Петербург'
        self.location.save()
        updated_location = Location.objects.get(pk=self.location.pk)
        self.assertEqual(updated_location.city, 'Санкт-Петербург')

    def test_model_deletion(self):
        self.location.delete()
        with self.assertRaises(Location.DoesNotExist):
            Location.objects.get(pk=self.location.pk)


class ThemeModelTestCase(TestCase):
    def test_model_creation(self):
        theme = Theme.objects.create(name='Тестовая тематика')
        self.assertIsNotNone(theme)

    def test_model_update(self):
        theme = Theme.objects.create(name='Тестовая тематика')
        theme.name = 'Новая тематика'
        theme.save()
        updated_theme = Theme.objects.get(pk=theme.pk)
        self.assertEqual(updated_theme.name, 'Новая тематика')

    def test_model_deletion(self):
        theme = Theme.objects.create(name='Тестовая тематика')
        theme.delete()
        with self.assertRaises(Theme.DoesNotExist):
            Theme.objects.get(pk=theme.pk)


class EventModelTestCase(TestCase):
    def setUp(self):
        self.location = Location.objects.create(
            city='Москва',
            address='ул. Примерная, д. 123',
            builing='Конференц-центр "Пример"',
            metro_station='Станция "Примерная"'
        )
        self.theme = Theme.objects.create(name='Тестовая тематика')

    def test_model_creation(self):
        event = Event.objects.create(
            name='Тестовое мероприятие',
            date_time_start=datetime.now(),
            location=self.location,
            max_participants=100,
            event_type='Конференция',
            activity_status='Активно',
            theme=self.theme
        )
        self.assertIsNotNone(event)

    def test_model_update(self):
        event = Event.objects.create(
            name='Тестовое мероприятие',
            date_time_start=datetime.now(),
            location=self.location,
            max_participants=100,
            event_type='Конференция',
            activity_status='Активно',
            theme=self.theme
        )
        event.name = 'Новое мероприятие'
        event.save()
        updated_event = Event.objects.get(pk=event.pk)
        self.assertEqual(updated_event.name, 'Новое мероприятие')

    def test_model_deletion(self):
        event = Event.objects.create(
            name='Тестовое мероприятие',
            date_time_start=datetime.now(),
            location=self.location,
            max_participants=100,
            event_type='Конференция',
            activity_status='Активно',
            theme=self.theme
        )
        event.delete()
        with self.assertRaises(Event.DoesNotExist):
            Event.objects.get(pk=event.pk)


class PhotoModelTestCase(TestCase):
    def setUp(self):
        self.location = Location.objects.create(
            city='Москва',
            address='ул. Примерная, д. 123',
            builing='Конференц-центр "Пример"',
            metro_station='Станция "Примерная"'
        )
        self.theme = Theme.objects.create(name='Тестовая тематика')
        self.event = Event.objects.create(
            name='Тестовое мероприятие',
            date_time_start=datetime.now(),
            location=self.location,
            max_participants=100,
            event_type='Конференция',
            activity_status='Активно',
            theme=self.theme
        )

    def test_model_creation(self):
        photo = Photo.objects.create(
            file='test_photo.jpg',
            event=self.event
        )
        self.assertIsNotNone(photo)

    def test_model_update(self):
        photo = Photo.objects.create(
            file='test_photo.jpg',
            event=self.event
        )
        photo.file = 'updated_photo.jpg'
        photo.save()
        updated_photo = Photo.objects.get(pk=photo.pk)
        self.assertEqual(updated_photo.file, 'updated_photo.jpg')

    def test_model_deletion(self):
        photo = Photo.objects.create(
            file='test_photo.jpg',
            event=self.event
        )
        photo.delete()
        with self.assertRaises(Photo.DoesNotExist):
            Photo.objects.get(pk=photo.pk)


class SpeakerModelTestCase(TestCase):
    def test_model_creation(self):
        speaker = Speaker.objects.create(
            name='Тестовый спикер',
            job='Тестовая должность'
        )
        self.assertIsNotNone(speaker)

    def test_model_update(self):
        speaker = Speaker.objects.create(
            name='Тестовый спикер',
            job='Тестовая должность'
        )
        speaker.name = 'Обновленный спикер'
        speaker.save()
        updated_speaker = Speaker.objects.get(pk=speaker.pk)
        self.assertEqual(updated_speaker.name, 'Обновленный спикер')

    def test_model_deletion(self):
        speaker = Speaker.objects.create(
            name='Тестовый спикер',
            job='Тестовая должность'
        )
        speaker.delete()
        with self.assertRaises(Speaker.DoesNotExist):
            Speaker.objects.get(pk=speaker.pk)


class ProgramModelTestCase(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Test Speaker',
            job='Test Position'
        )
        self.event = Event.objects.create(
            name='Test Event',
            date_time_start=timezone.now(),
            max_participants=100,
            activity_status='active'
        )

    def test_model_creation(self):
        program = Program.objects.create(
            name='Test Program',
            date_time=timezone.now(),
            speaker=self.speaker,
            event=self.event,
            material='test_material.txt'
        )
        self.assertIsNotNone(program)

    def test_model_update(self):
        program = Program.objects.create(
            name='Test Program',
            date_time=timezone.now(),
            speaker=self.speaker,
            event=self.event,
            material='test_material.txt'
        )
        program.name = 'Updated Test Program'
        program.save()
        updated_program = Program.objects.get(pk=program.pk)
        self.assertEqual(updated_program.name, 'Updated Test Program')

    def test_model_deletion(self):
        program = Program.objects.create(
            name='Test Program',
            date_time=timezone.now(),
            speaker=self.speaker,
            event=self.event,
            material='test_material.txt'
        )
        program.delete()
        with self.assertRaises(Program.DoesNotExist):
            Program.objects.get(pk=program.pk)


class UserEventModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.event = Event.objects.create(name='Test Event')

    def test_model_creation(self):
        user_event = UserEvent.objects.create(
            user=self.user,
            event=self.event,
            agree=True
        )
        self.assertIsNotNone(user_event)

    def test_model_update(self):
        user_event = UserEvent.objects.create(
            user=self.user,
            event=self.event,
            agree=True
        )
        user_event.agree = False
        user_event.save()
        updated_user_event = UserEvent.objects.get(pk=user_event.pk)
        self.assertFalse(updated_user_event.agree)

    def test_model_deletion(self):
        user_event = UserEvent.objects.create(
            user=self.user,
            event=self.event,
            agree=True
        )
        user_event.delete()
        with self.assertRaises(UserEvent.DoesNotExist):
            UserEvent.objects.get(pk=user_event.pk)
