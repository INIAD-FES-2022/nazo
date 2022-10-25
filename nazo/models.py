from email.policy import default
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
import uuid

# Create your models here.

class Nazo(models.Model):
    title = models.CharField(max_length=30, verbose_name="タイトル文")
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True, primary_key=True)
    difficulty = models.IntegerField()
    input = models.CharField(max_length=10, verbose_name="入力方法指定")
    minihint = models.TextField(verbose_name="ミニヒント文")
    hint = models.TextField(verbose_name="不正解時ヒント文")
    big_hint = models.TextField(verbose_name="クソデカ大ヒント文（すごい）")
    img = models.ImageField(upload_to="nazo/", verbose_name="謎解き画像")
    tutorial = models.BooleanField(default=False, verbose_name="チュートリアル")
    last_nazo = models.BooleanField(default=False, verbose_name="最終問題")

    def __str__(self):
        return self.title

class Answer(models.Model):
    input_answer = models.CharField(max_length=30, verbose_name="入力内容回答")
    keyword = models.CharField(max_length=20, verbose_name="最終問題のキーワード")
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True, primary_key=True)
    answer = models.TextField(verbose_name="回答")
    next_place = models.TextField(null=True,blank=True, verbose_name="次の謎の場所")
    img = models.ImageField(upload_to="answer/" ,verbose_name="キー画像")
    nazo_number = models.ForeignKey(Nazo, on_delete=models.CASCADE)
    border_color = models.CharField(max_length=10,verbose_name="答えのページの枠線の色")

    def __str__(self):
        return self.input_answer