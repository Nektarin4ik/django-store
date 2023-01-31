from django.contrib import admin

from users.models import EmailVerification, User

#
# @admin.register(User)
# class Users(admin.ModelAdmin):
#     list_display = ['__all__']
admin.site.register(User)


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ['code', 'user', 'expiration']
    fields = ('code', 'user', 'expiration', 'created')
    readonly_fields = ('created',)
