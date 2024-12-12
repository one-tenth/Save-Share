from django.contrib import admin
from .models import Member,Profile

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'phone', 'date_joined']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'member', 'bio']