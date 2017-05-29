# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adress = models.CharField(verbose_name = "adress", max_length = 50)
    zipcode = models.IntegerField(verbose_name = "zipcode")
    city = models.CharField(verbose_name = "city", max_length = 50)
    website = models.CharField(verbose_name = "website", max_length = 50)
    contact_email = models.EmailField(verbose_name = "contact_email", max_length = 50)
    avatar = models.ImageField(verbose_name = "avatar")
    skills = models.TextField(verbose_name = "skills", max_length = 500)
    interests = models.TextField(verbose_name = "interests", max_length = 500)
