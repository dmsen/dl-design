# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-09-27 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20200927_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linsystemuser',
            name='userPic',
            field=models.ImageField(default='./linSystem/defaultTou.png', upload_to='./linSystem/%Y/%m%d/', verbose_name='用户头像'),
        ),
    ]
