from django.contrib import admin

from events.models import (
    Event,
    Location,
    Photo,
    Program,
    Speaker,
    Theme,
    UserEvent
)


class ProgramInline(admin.StackedInline):
    model = Program
    extra = 0


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 0


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'location_id', 'city', 'address', 'builing', 'metro_station'
    )


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = (
        'theme_id', 'name'
    )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'event_id', 'name', 'date_time', 'location', 'max_participants',
        'information', 'event_type', 'event_format', 'activity_status',
        'wallpaper', 'theme', 'video', 'status', 'curent_participants'
    )
    readonly_fields = ('status',)

    inlines = [ProgramInline, PhotoInline]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        'photo_id', 'file', 'event'
    )


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = (
        'speaker_id', 'name', 'job', 'avatar'
    )


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = (
        'program_id', 'name', 'date_time', 'speaker', 'information', 'event',
        'material'
    )


@admin.register(UserEvent)
class UserEventAdmin(admin.ModelAdmin):
    list_display = (
        'user_event_id', 'user', 'event', 'agree'
    )
