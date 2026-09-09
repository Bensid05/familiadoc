from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Document

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Informations Familiales', {'fields': ('role',)}),
    )
    list_display = ['username', 'email', 'role', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Document)