from email.policy import default
from tabnanny import verbose
from django.db import models

# Create your models here.

class Event(models.Model):
    event = models.BooleanField(default=False, verbose_name="開催")

class Search(models.Model):
    title = models.TextField(verbose_name="タイトル")
    text = models.TextField(verbose_name="本文")
    memo = models.CharField(max_length=30, verbose_name="メモ")
    limit = models.CharField(max_length=30, verbose_name="制限時間")
    wait = models.BooleanField(default=False, verbose_name="待機画面用か")
    show = models.BooleanField(default=False, verbose_name="開催時公開")

    def __str__(self):
        return self.memo