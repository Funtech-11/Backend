from django.contrib import admin

from events.models import (
    Event,
    Location,
    Program,
    Speaker,
    Theme,
)


class ProgramInline(admin.StackedInline):
    model = Program
    extra = 0


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'event_id', 'name', 'date_time', 'location', 'number_of_participants',
        'information', 'event_type', 'event_format', 'status',
        'activity_status', 'wallpaper', 'theme'
    )

    inlines = [ProgramInline]


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = (
        'program_id', 'name', 'date_time', 'speaker', 'information', 'event'
    )


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = (
        'theme_id', 'name'
    )


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'location_id', 'city', 'address', 'builing', 'metro_station'
    )


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = (
        'speaker_id', 'name', 'job', 'avatar'
    )
