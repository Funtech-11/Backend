from rest_framework import serializers

from events.enums import (
    EventActivityStatusEnum,
    EventFormatEnum,
    EventTypeEnum
)
from events.models import Event, Location, Program, Speaker, Theme, UserEvent


class LocationSerializer(serializers.ModelSerializer):
    locationId = serializers.IntegerField(
        source='location_id',
        required=False
    )
    metroStation = serializers.CharField(
        source='metro_station',
        required=False
    )

    class Meta:
        model = Location
        fields = [
            'locationId', 'city', 'address', 'builing', 'metroStation'
        ]
        extra_kwargs = {
            'locationId': {'required': False},
            'metroStation': {'required': False}
        }


class ThemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Theme
        fields = [
             'name'
        ]
        extra_kwargs = {
            'themeId': {'required': False}
        }


class SpeakerSerializer(serializers.ModelSerializer):
    speakerId = serializers.IntegerField(
        source='speaker_id',
        required=False
    )

    class Meta:
        model = Speaker
        fields = [
            'speakerId', 'name', 'job', 'avatar'
        ]
        extra_kwargs = {
            'speakerId': {'required': False}
        }


class ProgramSerializer(serializers.ModelSerializer):
    speaker = SpeakerSerializer()

    programId = serializers.IntegerField(
        source='program_id',
        required=False
    )
    dateTime = serializers.DateTimeField(
        source='date_time'
    )

    class Meta:
        model = Program
        fields = [
            'programId', 'name', 'dateTime', 'speaker', 'information',
            'material'
        ]
        extra_kwargs = {
            'programId': {'required': False}
        }


class EventSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    theme = ThemeSerializer(
        read_only=True
    )
    programs = ProgramSerializer(
        many=True,
        read_only=True
    )
    eventId = serializers.IntegerField(
        source='event_id',
        required=False
    )
    dateTimeStart = serializers.DateTimeField(
        source='date_time_start'
    )
    dateTimeEnd = serializers.DateTimeField(
        source='date_time_end',
        required=False
    )
    maxParticipants = serializers.IntegerField(
        source='max_participants'
    )
    curentParticipants = serializers.IntegerField(
        source='curent_participants',
        read_only=True
    )
    eventType = serializers.ChoiceField(
        choices=[e_type.name for e_type in EventTypeEnum],
        source='event_type'
    )
    eventFormat = serializers.ChoiceField(
        choices=[e_format.name for e_format in EventFormatEnum],
        source='event_format'
    )
    activityStatus = serializers.ChoiceField(
        choices=[e_act_stat.name for e_act_stat in EventActivityStatusEnum],
        source='activity_status'
    )
    video = serializers.URLField(
        required=False
    )

    class Meta:
        model = Event
        fields = [
            'eventId', 'name', 'dateTimeStart', 'dateTimeEnd', 'location',
            'maxParticipants', 'curentParticipants', 'information',
            'eventType', 'eventFormat', 'status', 'activityStatus',
            'wallpaper', 'theme', 'video', 'programs'
        ]
        extra_kwargs = {
            'eventId': {'required': False}
        }


class UserEventSerializer(serializers.ModelSerializer):
    # user
    event = EventSerializer()

    userEventId = serializers.IntegerField(
        source='user_event_id'
    )

    class Meta:
        model = UserEvent
        fields = [
            'userEventId', 'user', 'event', 'agree'
        ]
        extra_kwargs = {
            'userEventId': {'required': False}
        }
