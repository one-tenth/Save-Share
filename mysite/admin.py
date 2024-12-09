from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Member

class MemberAdmin(UserAdmin):
    list_display=['id','username','email','phone','date_joined']

admin.site.register(Member, MemberAdmin)