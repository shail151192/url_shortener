# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import random

# Create your models here.

class Kgs(models.Model):
    key = models.CharField(max_length=6, unique=True)
    used = models.BooleanField(default=False)

    @classmethod
    def get_available_keys(cls):
        return 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZX'

    @classmethod
    def create_short_keys(cls):
        str = cls.get_available_keys()
        obs = []
        last_id = Kgs.objects.last()
        if not last_id:
            last_id = 0
        else:
            last_id = last_id.id
        for i in range(0, 5000):
            key = (str[random.randint(0, 62)] + str[random.randint(0, 62)] + str[random.randint(0, 62)] + str[random.randint(0, 62)] +str[random.randint(0, 62)]+str[random.randint(0, 62)])
            ob = Kgs(id=last_id+1, key=key, used=False)
            obs.append(ob)
            last_id += 1
        Kgs.objects.bulk_create(obs)




