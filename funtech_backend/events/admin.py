from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'event_id', 'name', 'date', 'time', 'city', 'address',
        'number_of_paricipants', 'information', 'event_type', 'event_format',
        'theme', 'program_time', 'program_name', 'program_speaker',
        'program_information', 'status', 'activity_status',
    )
