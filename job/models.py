from django.db import models
from accounts.models import User

# Create your models here.

class Post_job(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject = models.CharField('제목', max_length=100)
    create_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)
    server = models.CharField('서버', max_length=10)
    boss = models.CharField('보스', max_length=20)
    level = models.CharField('난이도', max_length=10)
    total = models.PositiveIntegerField('인원')
    job = models.CharField('직업', max_length=10, null=True, blank=True)
    content = models.TextField()
    kind = models.BooleanField('구인/구직', default=True)
    is_complete = models.BooleanField('완료여부', default=False)
    ct_id = models.PositiveIntegerField('content_type_id', default=13)