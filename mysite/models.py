# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class Member(AbstractUser):
    # 例如新增手機號碼欄位
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    # OneToOneField 連接到 Member 模型
    member = models.OneToOneField(
        Member,
        on_delete=models.CASCADE,  # 如果 Member 被刪除，Profile 也會被刪除
        related_name='profile'     # Member 反向查詢時的名稱
    )
    bio = models.TextField(blank=True, null=True)  # 簡介

    def __str__(self):
        return f"{self.member.username}'s Profile"