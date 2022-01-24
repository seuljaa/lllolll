from django.db import models
from accounts.models import User

# Create your models here.

class DealItems(models.Model):
    STAR_FORCE_CHOICES = (
        ('해당없음', '해당없음'),
        ('17성 이하', '17성 이하'),
        ('17성 초과', '17성 초과'),
    )

    ABILITY_CHOICES = (
        ('해당없음', '해당없음'),
        ('에픽', '에픽'),
        ('유니크', '유니크'),
        ('레전드리', '레전드리'),
    )

    SERVER_CHOICES = (
        ('베라', '베라'),
        ('스카니아', '스카니아'),
        ('루나', '루나'),
        ('제니스', '제니스'),
        ('크로아', '크로아'),
        ('유니온', '유니온'),
        ('엘리시움', '엘리시움'),
        ('이노시스', '이노시스'),
        ('레드', '레드'),
        ('오로라', '오로라'),
        ('아케인', '아케인'),
        ('노바', '노바'),
    )

    GROUP_CHOICES = (
        ('전사', '전사'),
        ('마법사', '마법사'),
        ('궁수', '궁수'),
        ('도적', '도적'),
        ('해적', '해적'),
    )

    Armor_CHOICES = (
        ('모자', '모자'),
        ('상의', '상의'),
        ('하의', '하의'),
        ('한벌옷', '한벌옷'),
        ('장갑', '장갑'),
        ('망토', '망토'),
        ('신발', '신발'),
    )

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject = models.CharField('제목', max_length=100)
    create_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)
    server = models.CharField('서버', max_length=10, choices=SERVER_CHOICES)
    group = models.CharField('직업군', max_length=10, choices=GROUP_CHOICES)
    part = models.CharField('부위', max_length=10,choices=Armor_CHOICES)
    price = models.PositiveIntegerField('가격')
    price_kind = models.BooleanField('억/엄', default=True)
    star_force = models.CharField('스타포스', max_length=9, choices=STAR_FORCE_CHOICES)
    ability_1 = models.CharField('윗잠', max_length=9, choices=ABILITY_CHOICES)
    ability_2 = models.CharField('아랫잠', max_length=9, choices=ABILITY_CHOICES)
    content = models.TextField()
    sale_buy = models.BooleanField('삼/팜', default=True)
    is_complete = models.BooleanField('완료여부', default=False)
