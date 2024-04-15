from django.test import TestCase
from users.models import User, Agreement, UserAgreement, Expertise, Stack, UserExpertise


class UserModelTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'test_user',
            'first_name': 'Иван',
            'last_name': 'Иванов',
            'email': 'test@example.com',
            'mobile_number': 1234567890,
            'employment': 'Test Company',
            'position': 'Test Position',
            'experience': 'Начальный',
            'preferred_format': 'Вебинар',
        }

    def test_create_user(self):
        user = User.objects.create(**self.user_data)
        self.assertIsNotNone(user)
        self.assertEqual(user.username, 'test_user')

    def test_update_user(self):
        user = User.objects.create(**self.user_data)
        updated_data = {'first_name': 'Новое имя'}
        User.objects.filter(username='test_user').update(**updated_data)
        user.refresh_from_db()
        self.assertEqual(user.first_name, 'Новое имя')

    def test_delete_user(self):
        User.objects.filter(username='test_user').delete()
        self.assertFalse(User.objects.filter(username='test_user').exists())


class AgreementModelTestCase(TestCase):
    def setUp(self):
        self.agreement_data = {
            'text': 'Текст тестового соглашения',
            'is_required': True,
        }

    def test_create_agreement(self):
        agreement = Agreement.objects.create(**self.agreement_data)
        self.assertIsNotNone(agreement)
        self.assertEqual(agreement.text, 'Текст тестового соглашения')

    def test_update_agreement(self):
        agreement = Agreement.objects.create(**self.agreement_data)
        updated_data = {'text': 'Новый текст соглашения'}
        Agreement.objects.filter(text='Текст тестового соглашения').update(
            **updated_data
        )
        agreement.refresh_from_db()
        self.assertEqual(agreement.text, 'Новый текст соглашения')

    def test_delete_agreement(self):
        Agreement.objects.filter(text='Текст тестового соглашения').delete()
        self.assertFalse(Agreement.objects.filter(
            text='Текст тестового соглашения'
        ).exists())


class UserAgreementModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.agreement = Agreement.objects.create(
            text='Текст тестового соглашения', is_required=True
        )

    def test_create_user_agreement(self):
        user_agreement = UserAgreement.objects.create(
            agreement=self.agreement, user=self.user, is_signed=True
        )
        self.assertIsNotNone(user_agreement)
        self.assertEqual(
            user_agreement.agreement.text, 'Текст тестового соглашения'
        )
        self.assertEqual(user_agreement.user.username, 'test_user')
        self.assertTrue(user_agreement.is_signed)

    def test_update_user_agreement(self):
        user_agreement = UserAgreement.objects.create(
            agreement=self.agreement, user=self.user, is_signed=True
        )
        updated_data = {'is_signed': False}
        UserAgreement.objects.filter(
            agreement=self.agreement, user=self.user
        ).update(**updated_data)
        user_agreement.refresh_from_db()
        self.assertFalse(user_agreement.is_signed)

    def test_delete_user_agreement(self):
        UserAgreement.objects.filter(
            agreement=self.agreement, user=self.user
        ).delete()
        self.assertFalse(UserAgreement.objects.filter(
            agreement=self.agreement, user=self.user
        ).exists())


class ExpertiseModelTestCase(TestCase):
    def setUp(self):
        self.expertise = Expertise.objects.create(name='Тестовая экспертиза')

    def test_create_expertise(self):
        expertise = Expertise.objects.create(name='Новая экспертиза')
        self.assertIsNotNone(expertise)
        self.assertEqual(expertise.name, 'Новая экспертиза')

    def test_update_expertise(self):
        self.expertise.name = 'Обновленная экспертиза'
        self.expertise.save()
        updated_expertise = Expertise.objects.get(pk=self.expertise.pk)
        self.assertEqual(updated_expertise.name, 'Обновленная экспертиза')

    def test_delete_expertise(self):
        expertise = Expertise.objects.create(name='Экспертиза для удаления')
        expertise.delete()
        self.assertFalse(Expertise.objects.filter(
            name='Экспертиза для удаления'
        ).exists())


class StackModelTestCase(TestCase):
    def setUp(self):
        self.stack = Stack.objects.create(name='Тестовый стек')

    def test_create_stack(self):
        stack = Stack.objects.create(name='Новый стек')
        self.assertIsNotNone(stack)
        self.assertEqual(stack.name, 'Новый стек')

    def test_update_stack(self):
        self.stack.name = 'Обновленный стек'
        self.stack.save()
        updated_stack = Stack.objects.get(pk=self.stack.pk)
        self.assertEqual(updated_stack.name, 'Обновленный стек')

    def test_delete_stack(self):
        stack = Stack.objects.create(name='Стек для удаления')
        stack.delete()
        self.assertFalse(Stack.objects.filter(
            name='Стек для удаления'
        ).exists())


class UserExpertiseModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.expertise = Expertise.objects.create(name='Тестовая экспертиза')
        self.stack = Stack.objects.create(name='Тестовый стек')
        self.user_expertise = UserExpertise.objects.create(
            user=self.user, expertise=self.expertise, stack=self.stack
        )

    def test_create_user_expertise(self):
        user_expertise = UserExpertise.objects.create(
            user=self.user, expertise=self.expertise, stack=self.stack
        )
        self.assertIsNotNone(user_expertise)
        self.assertEqual(user_expertise.user, self.user)
        self.assertEqual(user_expertise.expertise, self.expertise)
        self.assertEqual(user_expertise.stack, self.stack)

    def test_update_user_expertise(self):
        self.user_expertise.stack = Stack.objects.create(
            name='Обновленный стек'
        )
        self.user_expertise.save()
        updated_user_expertise = UserExpertise.objects.get(
            pk=self.user_expertise.pk
        )
        self.assertEqual(
            updated_user_expertise.stack.name, 'Обновленный стек'
        )

    def test_delete_user_expertise(self):
        user_expertise = UserExpertise.objects.create(
            user=self.user, expertise=self.expertise, stack=self.stack
        )
        user_expertise.delete()
        self.assertFalse(UserExpertise.objects.filter(
            pk=user_expertise.pk
        ).exists())
