from django.contrib import admin

from events.models import Event, Program, EventTheme, Theme


class ProgramInline(admin.StackedInline):
    model = Program
    extra = 0


class EventThemeInline(admin.StackedInline):
    model = EventTheme
    extra = 0


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'event_id', 'name', 'date', 'time', 'city', 'address',
        'number_of_paricipants', 'information', 'event_type', 'event_format',
        'status', 'activity_status',
    )

    inlines = [ProgramInline, EventThemeInline]


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('pk', 'time', 'speaker', 'information', 'event')


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
