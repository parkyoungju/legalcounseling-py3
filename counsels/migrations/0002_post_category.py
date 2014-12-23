# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counsels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('CAR_ACCIDENT', '교통사고 과실 비율 추정'), ('CERTIFICATION', '내용증명, 고소장 작성'), ('REQUEST_ADVICE', '법률 상담 의뢰'), ('COUNSELING', '간편 법률 상담')], max_length=100, default='COUNSELING'),
            preserve_default=True,
        ),
    ]
