from enum import Enum


class EventTypeEnum(Enum):
    OFFLINE = 'offline'
    ONLINE = 'online'


class EventFormatEnum(Enum):
    CONFERENCE = 'conference'
    MEETUP = 'meetup '
    NETWORKING = 'networking'
    EXCURSION = 'excursion'


class EventStatusEnum(Enum):
    REGISTRATION_OPEN = 'registration_open'
    REGISTRATION_CLOSE = 'registration_close'
    FINISHED = 'finished'


class EventActivityStatusEnum(Enum):
    DRAFT = 'draft'
    ACTIVE_EVENT = 'active_event'


class EventThemeEnum(Enum):
    PROGRAMMING = 'Разработка'
    DESIGN = 'Дизайн '
    MANAGEMENT = 'Менеджмент'
    MARKETING = 'Маркетинг'
    ANALYTICS = 'Аналитика'
    BUSINESS = 'Бизнес'
    OTHER = 'Другое'
