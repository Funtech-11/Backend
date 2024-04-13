from rest_framework import serializers

from users.models import (
    User,
    Agreement,
    UserAgreement,
    Expertise,
    Stack,
    UserExpertise
)

from events.models import UserEvent

""" Сериализаторы объектов, которые создает админ. """
""" ПРОВЕРКА """


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
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('username', instance.username)
        instance.text = validated_data.get('email', instance.email)
#        agreements = validated_data.pop('user_agreements')
#        programmes = validated_data.pop('user_expertise')
#        if agreements:
#            for item in agreements:
#                UserAgreement.objects.create(user=self.context['request'].user,
#                                             agreement=item['agreement'],
#                                             is_signed=item['is_signed'])
        print(validated_data)
        user_data = validated_data.pop('userExper')
        user = validated_data.pop('user')
        UserExpertise.objects.filter(user=user).delete()
        for item in user_data:
            for stack_item in item['stack']:
                UserExpertise.objects.create(stack_id=stack_item,
                                            expertise_id=item['expertise']['pk'],
                                            user=user)

        instance.save()
        print(User.objects.get(pk=1))
        us = User.objects.get(pk=1)
        print(us.userExper.all())
        return instance

    def to_representation(self, instance):
        serializers = UserDetailSerializer(instance, context=self.context)
        return serializers.data


class TicketSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = UserEvent
        fields = '__all__'
        read_only_fields = ('__all__',)
