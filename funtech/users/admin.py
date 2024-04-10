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
    list_display = (
        'first_name', 'last_name', 'mobile_number', 'employment', 'position',
        'experience', 'preferred_format'
    )
    inlines = [UserAgreementInline]


@admin.register(Agreement)
class AgreementAdmin(admin.ModelAdmin):
    list_display = (
        'text', 'link'
    )


@admin.register(UserAgreement)
class UserAgreementAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'agreement'
    )


@admin.register(Expertise)
class ExpertiseAdmin(admin.ModelAdmin):
    list_display = (
       'name',
    )


@admin.register(Stack)
class StackAdmin(admin.ModelAdmin):
    list_display = (
       'name', 'expertise'
    )


@admin.register(UserExpertise)
class UserExpertiseAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'expertise', 'stack'
    )
