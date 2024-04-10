from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import (
    Agreement,
    Expertise,
    Stack, User,
    UserAgreement,
    UserExpertise
)


class UserAgreementInline(admin.StackedInline):
    model = UserAgreement
    extra = 0


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ('last_name',)


@admin.register(UserExpertise)
class UserExpertiseAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'expertise', 'stack'
    )
