from django.contrib import admin

from events.models import Event, EventTheme, Location, Program, Theme, Video


class ProgramInline(admin.StackedInline):
    model = Program
    extra = 0


class EventThemeInline(admin.StackedInline):
    model = EventTheme
    extra = 0


# class MatetialInline(admin.StackedInline):
#     model = Matetial
#     extra = 0


class VideoInline(admin.StackedInline):
    model = Video
    extra = 0


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'event_id', 'name', 'date_time', 'location', 'number_of_participants',
        'information', 'event_type', 'event_format', 'status',
        'activity_status', 'wallpaper', 'amount_programs', 'amount_themes'
    )

    inlines = [ProgramInline, EventThemeInline, VideoInline]

    def amount_programs(self, obj):
        return obj.programs.count()

    def amount_themes(self, obj):
        return obj.themes.count()

    amount_programs.short_description = 'Кол-во программ'
    amount_themes.short_description = 'Кол-во тематик'


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'time', 'speaker', 'information', 'event'
    )


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'name'
    )

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'location_id', 'city', 'address', 'builing', 'metro_station'
    )
