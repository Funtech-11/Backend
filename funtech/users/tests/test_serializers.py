from django.test import TestCase
from users.models import (
    Agreement,
    AuthUser,
    Event,
    Expertise,
    Stack,
    User,
    UserAgreement,
    UserEvent,
    UserExpertise,
)
from users.serializers import (
    AgreementSerializer,
    ExpertiseSerializer,
    StackDetailSerializer,
    StackSerializer,
    TicketSerializer,
    UserAgreementSerializer,
    UserDetailSerializer,
    UserEventCreateSerializer,
    UserEventSerializer,
    UserExpertiseDetailSerializer,
    UserExpertiseSerializer,
    UserSerializer,
)


class AgreementSerializerTestCase(TestCase):
    def test_serializer_fields(self):
        serializer = AgreementSerializer()
        self.assertEqual(serializer.Meta.model, Agreement)
        self.assertEqual(serializer.Meta.fields, '__all__')


class StackSerializerTestCase(TestCase):
    def setUp(self):
        self.stack_data = {
            'name': 'Тестовый стек'
        }
        self.serializer_with_data = StackSerializer(data=self.stack_data)
        self.serializer_without_data = StackSerializer(data={})

    def test_serializer_with_valid_data(self):
        self.assertTrue(self.serializer_with_data.is_valid())

    def test_serializer_without_data(self):
        self.assertFalse(self.serializer_without_data.is_valid())

    def test_serializer_save_method(self):
        self.serializer_with_data.is_valid()
        stack = self.serializer_with_data.save()
        self.assertIsNotNone(stack)
        self.assertEqual(stack.name, 'Тестовый стек')


class StackDetailSerializerTestCase(TestCase):
    def setUp(self):
        self.stack = Stack.objects.create(name='Тестовый стек')
        self.expertise = Expertise.objects.create(name='Тестовая экспертиза')

    def test_serializer_fields(self):
        serializer = StackDetailSerializer(
            instance={'stack': self.stack, 'expertise': self.expertise}
        )
        expected_data = {
            'id': self.stack.pk,
            'name': self.stack.name,
            'expertise': self.expertise.name
        }
        self.assertEqual(serializer.data, expected_data)


class ExpertiseSerializerTestCase(TestCase):
    def test_create_expertise_serializer(self):
        serializer = ExpertiseSerializer(data={'name': 'Тестовая экспертиза'})
        self.assertTrue(serializer.is_valid())

    def test_update_expertise_serializer(self):
        expertise = Expertise.objects.create(name='Тестовая экспертиза')
        serializer = ExpertiseSerializer(
            instance=expertise,
            data={'name': 'Обновленная экспертиза'},
            partial=True
        )
        self.assertTrue(serializer.is_valid())

    def test_invalid_expertise_serializer(self):
        serializer = ExpertiseSerializer(data={})
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)

    def test_valid_expertise_serializer(self):
        expertise = Expertise.objects.create(name='Тестовая экспертиза')
        serializer = ExpertiseSerializer(instance=expertise)
        expected_fields = {'id', 'name', 'stacks'}
        self.assertEqual(set(serializer.data.keys()), expected_fields)


class UserExpertiseSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.expertise = Expertise.objects.create(name='Тестовая экспертиза')
        self.stack1 = Stack.objects.create(name='Тестовый стек 1')
        self.stack2 = Stack.objects.create(name='Тестовый стек 2')
        self.user_expertise = UserExpertise.objects.create(
            user=self.user, expertise=self.expertise, stack=self.stack1
        )

    def test_user_expertise_serializer(self):
        data = {
            'user': self.user.pk,
            'expertise': self.expertise.pk,
            'stack': [self.stack1.pk, self.stack2.pk]
        }
        serializer = UserExpertiseSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        user_expertise = serializer.save()

        self.assertEqual(user_expertise.user, self.user)
        self.assertEqual(user_expertise.expertise, self.expertise)
        self.assertCountEqual(
            user_expertise.stack.all(), [self.stack1, self.stack2]
        )


class UserExpertiseDetailSerializerTestCase(TestCase):
    def test_serializer_fields(self):
        serializer = UserExpertiseDetailSerializer()

        expected_fields = ['id', 'name']
        serialized_fields = list(serializer.fields.keys())

        self.assertEqual(expected_fields, serialized_fields)


class UserAgreementSerializerTestCase(TestCase):
    def setUp(self):
        self.user_agreement_data = {
            "agreement": 1,
            "is_signed": True
        }
        self.serializer = UserAgreementSerializer(
            data=self.user_agreement_data
        )

    def test_serializer_with_valid_data(self):
        self.assertTrue(self.serializer.is_valid())

    def test_serializer_with_invalid_data(self):
        invalid_data = {
            "agreement": "invalid_pk",
            "is_signed": "not_a_boolean"
        }
        serializer_with_invalid_data = UserAgreementSerializer(
            data=invalid_data
        )
        self.assertFalse(serializer_with_invalid_data.is_valid())

    def test_serializer_save_method(self):
        if self.serializer.is_valid():
            user_agreement_instance = self.serializer.save(user=self.user)
            self.assertIsNotNone(user_agreement_instance)


class UserDetailSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='test_user',
            first_name='John',
            last_name='Doe',
            email='john@example.com',
            employment='Company XYZ',
            mobile_number='123456789',
            photo='photo.jpg',
            preferred_format='WEBINAR'
        )
        self.expertise = Expertise.objects.create(name='Test Expertise')
        self.stack = Stack.objects.create(name='Test Stack')
        self.user_expertise = UserExpertise.objects.create(
            user=self.user, expertise=self.expertise, stack=self.stack
        )
        self.agreement = UserAgreement.objects.create(
            text='Test Agreement', is_required=True
        )
        self.user_agreement = self.user.user_agreements.create(
            agreement=self.agreement, is_signed=True
        )

    def test_user_detail_serializer(self):
        serializer_data = UserDetailSerializer(instance=self.user).data
        self.assertEqual(serializer_data['id'], self.user.id)
        self.assertEqual(serializer_data['first_name'], self.user.first_name)
        self.assertEqual(serializer_data['last_name'], self.user.last_name)
        self.assertEqual(serializer_data['email'], self.user.email)
        self.assertEqual(serializer_data['workPlace'], self.user.employment)
        self.assertEqual(
            serializer_data['mobile_number'], self.user.mobile_number
        )
        self.assertEqual(serializer_data['photo'], self.user.photo)
        self.assertEqual(serializer_data['participationFormat'], 'WEBINAR')
        self.assertEqual(
            serializer_data['educationPrograms'][0]['name'], 'Test Expertise'
        )
        self.assertEqual(
            serializer_data['programStack'][0]['name'], 'Test Stack'
        )
        self.assertEqual(
            serializer_data['userAgreements'][0]['text'], 'Test Agreement'
        )
        self.assertEqual(
            serializer_data['userAgreements'][0]['is_signed'], True
        )


class UserSerializerTestCase(TestCase):
    def setUp(self):
        self.user = AuthUser.objects.create(
            username='test_user', email='test@example.com'
        )
        self.expertise = Expertise.objects.create(name='Тестовая экспертиза')
        self.stack = Stack.objects.create(name='Тестовый стек')
        self.user_expertise = UserExpertise.objects.create(
            user=self.user, expertise=self.expertise, stack=self.stack
        )
        self.agreement = UserAgreement.objects.create(
            user=self.user,
            agreement=self.user_expertise.expertise,
            is_signed=True
        )

    def test_serialization(self):
        serializer = UserSerializer(instance=self.user)
        data = serializer.data
        self.assertEqual(data['first_name'], self.user.first_name)
        self.assertEqual(data['last_name'], self.user.last_name)
        self.assertEqual(data['email'], self.user.email)
        self.assertEqual(data['mobile_number'], self.user.mobile_number)
        self.assertEqual(data['photo'], self.user.photo)
        self.assertEqual(data['workPlace'], self.user.employment)
        self.assertEqual(data['position'], self.user.position)
        self.assertEqual(data['experience'], self.user.experience)
        self.assertEqual(
            data['participationFormat'], self.user.preferred_format
        )
        self.assertEqual(
            data['userAgreements'][0]['is_signed'], self.agreement.is_signed
        )

    def test_update_method(self):
        serializer = UserSerializer(
            instance=self.user, data={'first_name': 'New', 'last_name': 'Name'}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'New')
        self.assertEqual(self.user.last_name, 'Name')

    def test_to_representation_method(self):
        serializer = UserSerializer(instance=self.user)
        data = serializer.data
        self.assertEqual(data['id'], self.user.id)
        self.assertEqual(data['first_name'], self.user.first_name)
        self.assertEqual(data['last_name'], self.user.last_name)
        self.assertEqual(data['email'], self.user.email)
        self.assertEqual(data['mobile_number'], self.user.mobile_number)
        self.assertEqual(data['photo'], self.user.photo)
        self.assertEqual(data['workPlace'], self.user.employment)
        self.assertEqual(data['position'], self.user.position)
        self.assertEqual(data['experience'], self.user.experience)
        self.assertEqual(
            data['participationFormat'], self.user.preferred_format
        )
        self.assertEqual(
            data['userAgreements'][0]['is_signed'], self.agreement.is_signed
        )


class TicketSerializerTestCase(TestCase):
    def setUp(self):
        self.user_event = UserEvent.objects.create(
            user_id=1, event_id=1, agree=True
        )
        self.serializer_data = {'user': 1, 'event': 1, 'agree': True}
        self.serializer = TicketSerializer(instance=self.user_event)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['user', 'event', 'agree'])

    def test_user_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['user'], self.user_event.user_id)

    def test_event_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['event'], self.user_event.event_id)

    def test_agree_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['agree'], self.user_event.agree)

    def test_create_valid_ticket(self):
        serializer = TicketSerializer(data=self.serializer_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_ticket(self):
        invalid_data = {'user': '', 'event': '', 'agree': ''}
        serializer = TicketSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())


class UserEventSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.event = Event.objects.create(name='Тестовое мероприятие')
        self.user_event = UserEvent.objects.create(
            user=self.user, event=self.event, agree=True
        )

    def test_serializer_fields(self):
        serializer = UserEventSerializer(instance=self.user_event)
        data = serializer.data
        self.assertEqual(
            set(data.keys()),
            {
                'user_event_id', 'user', 'event', 'agree', 'qr_code',
                'educationPrograms', 'userAgreements'
            }
        )

    def test_serializer_nested_fields(self):
        user_expertise = UserExpertise.objects.create(
            user=self.user, expertise=None, stack=None
        )
        user_agreement = UserAgreement.objects.create(
            user=self.user, text='Тестовое соглашение', is_signed=True
        )
        serializer = UserEventSerializer(instance=self.user_event)
        data = serializer.data
        self.assertEqual(len(data['educationPrograms']), 1)
        self.assertEqual(len(data['userAgreements']), 1)
        self.assertEqual(data['educationPrograms'][0]['id'], user_expertise.id)
        self.assertEqual(data['userAgreements'][0]['id'], user_agreement.id)


class UserEventCreateSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.agreement = Agreement.objects.create(
            text='Тестовое соглашение', is_required=True
        )
        self.event = Event.objects.create(name='Тестовое мероприятие')

    def test_user_event_create_serializer(self):
        data = {
            'user': self.user.id,
            'event': self.event.id,
            'agree': True
        }
        serializer = UserEventCreateSerializer(data=data)
        self.assertTrue(serializer.is_valid())
