from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ['username', 'id', 'borndate', 'gender', 'phoneNum']  # 確保列出你想顯示的字段

admin.site.register(Member, MemberAdmin)