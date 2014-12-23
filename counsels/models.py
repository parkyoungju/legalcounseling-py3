from django.db import models
from annoying.fields import AutoOneToOneField
from django.contrib.auth.models import User

class Profile(models.Model):
    user = AutoOneToOneField(User, primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    nickname = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)


class Post(models.Model):

    CATEGORY_CHOICE = (
        ('CAR_ACCIDENT', u'교통사고 과실 비율 추정'),
        ('CERTIFICATION', u'내용증명, 고소장 작성'),
        ('REQUEST_ADVICE', u'법률 상담 의뢰'),
        ('COUNSELING', u'간편 법률 상담'),
    )

    title = models.CharField(max_length=1000)
    content = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICE, default='COUNSELING')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)