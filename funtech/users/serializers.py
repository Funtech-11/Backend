from events.enums import EventTypeEnum
from events.models import UserEvent
from rest_framework import serializers

from users.models import (
    Agreement,
    Expertise,
    Stack,
    User,
    UserAgreement,
    UserExpertise,
)
from events.serializers import EventSerializer, UserEventSerializer

""" Сериализаторы объектов, которые создает админ. """


class AgreementSerializer(serializers.ModelSerializer):
    isRequired = serializers.BooleanField(
        source='is_required'
    )

    class Meta:
        model = Agreement
        fields = ('text', 'is_required')


class StackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = '__all__'


class StackDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='stack.pk')
    name = serializers.CharField(source='stack.name')
    expertise = serializers.CharField(source='expertise.name')

    class Meta:
        model = Stack
        fields = ('id', 'name', 'expertise')


class ExpertiseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expertise
        fields = '__all__'


""" Связующие сериализаторы. """


class UserExpertiseSerializer(serializers.ModelSerializer):
    expertise = serializers.CharField(source="expertise.name")
    stack = serializers.ListSerializer(child=StackSerializer())

    class Meta:
        model = UserExpertise
        fields = ('stack', 'expertise')


class UserExpertiseDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

    class Meta:
        model = Expertise
        fields = ('id', 'name')

    def to_representation(self, instance):
        print(instance, 11111111111111111111111)
        return super().to_representation(instance)


class UserAgreementSerializer(serializers.ModelSerializer):
    agreement = serializers.IntegerField(source="pk")
    isSigned = serializers.BooleanField(source='is_signed')

    class Meta:
        model = UserAgreement
        fields = ('agreement', 'user', 'isSigned')
        read_only_fields = ('user',)


""" Пользователь. """


class UserDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    firstName = serializers.CharField(source='first_name')
    email = serializers.EmailField()
    workPlace = serializers.CharField(source='employment')
    mobile_number = serializers.IntegerField()
    lastName = serializers.CharField(source='last_name')
    employment = serializers.CharField()
    photo = serializers.ImageField()
    participationFormat = serializers.ChoiceField(
        choices=[(choice.name, choice.value) for choice in EventTypeEnum],
        source='preferred_format'
    )
    educationPrograms = UserExpertiseDetailSerializer(
        many=True, source='expertise'
    )
    programStack = StackDetailSerializer(many=True, source='userExper')
    userAgreements = UserAgreementSerializer(many=True,
                                             source='user_agreements')

    # class Meta:
    #     model = User
    #     fields = (
    #         'id',
    #         'first_name',
    #         'last_name',
    #         'mobile_number',
    #         'photo',
    #         'workPlace',
    #         'position',
    #         'email',
    #         'educationPrograms',
    #         'programStack',
    #         'userAgreements'
    #     )


class UserSerializer(serializers.ModelSerializer):
    workPlace = serializers.CharField(source='employment')
    participationFormat = serializers.ChoiceField(
        choices=[(choice.name, choice.value) for choice in EventTypeEnum],
        source='preferred_format'
    )
    educationPrograms = UserExpertiseSerializer(many=True, source='userExper')
    userAgreements = UserAgreementSerializer(many=True,
                                             source='user_agreements')
    firstName = serializers.CharField(source='first_name')
    lastName = serializers.CharField(source='last_name')
    mobileNumber = serializers.IntegerField(source='mobile_number')

    class Meta:
        model = User
        fields = (
            'id',
            'firstName',
            'lastName',
            'email',
            'mobileNumber',
            'photo',
            'workPlace',
            'position',
            'experience',
            'participationFormat',
            'educationPrograms',
            # 'programStack',
            'userAgreements'
        )

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        if 'userAgreements' in validated_data:
            agreement = validated_data.pop('userAgreements')
        else:
            agreement = []
        print(validated_data)
        if 'userExper' in validated_data:
            user_data = validated_data.pop('userExper')
        else:
            user_data = []
        user = validated_data.pop('user')
        UserExpertise.objects.filter(user=user).delete()
        for item in user_data:
            for stack_item in item['stack']:
                UserExpertise.objects.create(
                    stack_id=stack_item,
                    expertise_id=item['expertise']['pk'],
                    user=user
                )

        for item in agreement:
            UserAgreement.objects.get_or_create(
                agreement_id=item['agreement'],
                is_signed=item['isSigned'],
                user=user
            )

        instance.save()
        return instance

    def to_representation(self, instance):
        values = Expertise.objects.filter(Exper__user=instance).distinct()
        instance.expertise = values
        serializers = UserDetailSerializer(instance, context=self.context)
        return serializers.data


class TicketSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    event = EventSerializer()
    userEventId = UserEventSerializer()
    qrCode = serializers.ImageField(source='qr_code')

    class Meta:
        model = UserEvent
        fields = ('userEventId', 'user', 'event', 'agree', 'qrCode')
        read_only_fields = ('__all__',)


class UserEventSerializer(serializers.ModelSerializer):

    educationPrograms = UserExpertiseSerializer(
        many=True, source='user.userExper'
    )
    userAgreements = UserAgreementSerializer(many=True,
                                             source='user.user_agreements')
    userEventId = serializers.IntegerField(source='user_event_id')
    qrCode = serializers.ImageField(source='qr_code')

    class Meta:
        model = UserEvent
        fields = (
            'userEventId',
            'user',
            'event',
            'agree',
            'qrCode',
            'educationPrograms',
            'userAgreements'
        )


class UserEventCreateSerializer(UserEventSerializer):
    userEventId = serializers.IntegerField(source='user_event_id')
    qrCode = serializers.ImageField(source='qr_code')

    class Meta:
        model = UserEvent
        fields = ('userEventId', 'user', 'event', 'agree', 'qrCode')
        read_only_fields = ('__all__',)
