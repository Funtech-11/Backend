from events.enums import EventTypeEnum
from rest_framework import serializers

from users.models import (
    Agreement,
    Expertise,
    Stack,
    User,
    UserAgreement,
    UserExpertise
)

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
    user = 
    expertise = 
    stack =

    class Meta:
        model = UserExpertise
        fields = '__all__'


class UserAgreementSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAgreement
        fields = '__all__'
        read_only_fields = ('user',)


""" Пользователь. """


class UserSerializer(serializers.ModelSerializer):
    workPlace = serializers.CharField(source='employment')
    participationFormat = serializers.ChoiceField(
        choices=[(choice.name, choice.value) for choice in EventTypeEnum],
        source='preferred_format'
    )
    educationPrograms = UserExpertiseSerializer(many=True,
                                                source='user_expertise')
    #programStack = StackSerializer(many=True)
    userAgreements = UserAgreementSerializer(many=True,
                                             source='user_agreements')

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'mobile_number',
            'photo',
            'workPlace',
            'position',
            'experience',
            'participationFormat',
            'educationPrograms',
            #'programStack',
            'userAgreements'
        )
    
    def update(self, instance, validated_data):
        agreements = validated_data.pop('user_agreements')
        programmes = validated_data.pop('user_expertise')
        if agreements:
            for item in agreements:
                UserAgreement.objects.create(user=self.context['request'].user,
                                             agreement=item['agreement'],
                                             is_signed=item['is_signed'])
        if programmes:
            for item in programmes:
                UserExpertise.objects.create()

        return super().update(instance, validated_data)