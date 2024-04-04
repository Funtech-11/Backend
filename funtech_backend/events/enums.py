from enum import Enum


class EventTypeEnum(Enum):
    OFFLINE = 'offline'
    ONLINE = 'online'


class EventFormatEnum(Enum):
    CONFERENCE = 'conference'
    MEETUP = 'meetup '
    NETWORKING = 'networking'
    EXCURSION = 'excursion'


class EventThemeEnum(Enum):
    PROGRAMMING = 'programming'
    DESIGN = 'design '
    MANAGEMENT = 'management'
    MARKETING = 'marketing'
    ANALYTICS = 'analytics'
    BUSINESS = 'business'
    OTHER = 'other'


class EventStatusEnum(Enum):
    REGISTRATION_OPEN = 'registration_open'
    REGISTRATION_CLOSE = 'registration_close'
    FINISHED = 'finished'


class EventActivityStatusEnum(Enum):
    DRAFT = 'draft'
    ACTIVE_EVENT = 'active_event'
