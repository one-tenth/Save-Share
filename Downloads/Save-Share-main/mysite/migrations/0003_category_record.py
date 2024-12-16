# Generated by Django 4.2.7 on 2024-12-15 06:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False, verbose_name='分類編號')),
                ('category_name', models.CharField(max_length=100, verbose_name='分類名稱')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('recordNo', models.AutoField(primary_key=True, serialize=False, verbose_name='紀錄編號')),
                ('transaction_type', models.CharField(choices=[('income', '收入'), ('expense', '支出')], default='expense', max_length=7, verbose_name='收支')),
                ('describe', models.TextField(verbose_name='說明')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='價格')),
                ('date', models.DateField(verbose_name='日期')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.category', verbose_name='商品類別')),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='會員編號')),
            ],
        ),
    ]