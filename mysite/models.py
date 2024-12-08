from django.db import models
from django.contrib.auth.models import *
# Create your models here.
class Member(AbstractUser):
    borndate = models.CharField(max_length=10, default='')
    # borndate = models.DateField(null=True, blank=True)
    Gender = (('M','男性'),('W',"女性"),)
    gender = models.CharField(max_length=5,choices=Gender)
    # phoneNum = models.CharField(max_length=10)
    phoneNum = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self):#看你要顯示啥 所以有可能是他的錯
        return  str(self.id)