from django.contrib import admin

from events.models import Event, Program, EventTheme, Theme, Matetial, Video


class ProgramInline(admin.StackedInline):
    model = Program
    extra = 0


class EventThemeInline(admin.StackedInline):
    model = EventTheme
    extra = 0


class MatetialInline(admin.StackedInline):
    model = Matetial
    extra = 0


class VideoInline(admin.StackedInline):
    model = Video
    extra = 0


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'event_id', 'name', 'date', 'time', 'city', 'address',
        'number_of_paricipants', 'information', 'event_type', 'event_format',
        'status', 'activity_status', 'amount_programs', 'amount_event_themes'
    )

    inlines = [ProgramInline, EventThemeInline, MatetialInline, VideoInline]

    def amount_programs(self, obj):
        return obj.programs.count()

    def amount_event_themes(self, obj):
        return obj.themes.count()

    amount_programs.short_description = 'Кол-во программ'
    amount_event_themes.short_description = 'Кол-во тематик'


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('pk', 'time', 'speaker', 'information', 'event')


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
