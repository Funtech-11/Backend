from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import User, UserAgreement


class UserAgreementInline(admin.StackedInline):
    model = UserAgreement
    extra = 0


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = [
        'first_name', 'last_name', 'email', 'mobile_number', 'photo',
        'employment', 'position', 'experience', 'preferred_format'
    ]
    fieldsets = (
        (
            'Main Fields', {
                'fields': (
                    'first_name', 'last_name', 'email', 'mobile_number',
                    'photo', 'employment', 'position', 'experience',
                    'preferred_format'
                ),
            }
        ),
    )
    ordering = ('last_name',)
