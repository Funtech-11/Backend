from rest_framework import serializers

from users.models import (
    User,
    Agreement,
    UserAgreement,
    Expertise,
    Stack,
    UserExpertise
)
from events.enums import EventTypeEnum

""" Сериализаторы объектов, которые создает админ. """


class AgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = '__all__'


class StackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = '__all__'


class ExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expertise
        fields = '__all__'


""" Связующие сериализаторы. """


class UserExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExpertise
        fields = '__all__'


class UserAgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAgreement
        fields = '__all__'


""" Пользователь. """


class UserSerializer(serializers.ModelSerializer):
    workPlace = serializers.CharField(source='employment')
    participationFormat = serializers.ChoiceField(
        choices=[(choice.name, choice.value) for choice in EventTypeEnum],
        source='preferred_format'
    )
    educationPrograms = ExpertiseSerializer(many=True)
    programStack = StackSerializer(many=True)
    userAgreement = UserAgreementSerializer()

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'mobile_number',
            'photo',
            'password',
            'workPlace',
            'position',
            'experience',
            'participationFormat',
            'educationPrograms',
            'programStack',
            'userAgreement'
        )

    def validate_programStack(self, value):
        # валидировать, что стэк принадлежит своему направлению
        pass
