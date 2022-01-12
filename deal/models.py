from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DealItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject = models.CharField('제목', max_length=100)
    create_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)
    server = models.CharField('서버', max_length=20)
    group = models.CharField('직업군', max_length=20)
    part = models.CharField('부위', max_length=20)
    price = models.PositiveIntegerField('가격')
    price_kind = models.BooleanField('억/엄', default=True)

    class Star_Force(models.Model):
        STAR_FORCE_CHOICES = (
            ('na', '해당없음'),
            ('under_17', '17성 이하'),
            ('up_17', '17성 초과'),
        )
        star_force =models.CharField(max_length=9, choices= STAR_FORCE_CHOICES)

    class Ability(models.Model):
        ABILITY_CHOICES = (
            ('na', '해당없음'),
            ('epic', '에픽'),
            ('unique', '유니크'),
            ('legendary', '레전드리'),
        )
        ability_1 = models.CharField(max_length=9, choices= ABILITY_CHOICES)
        ability_2 = models.CharField(max_length=9, choices= ABILITY_CHOICES)

    content = models.TextField()
    is_complete = models.BooleanField('완료여부', default=False)
