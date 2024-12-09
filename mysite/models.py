# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class Member(AbstractUser):
    # 例如新增手機號碼欄位
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username