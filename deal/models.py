from django.db import models
from accounts.models import User

# Create your models here.

class DealItems(models.Model):
    STAR_FORCE_CHOICES = (
        ('na', '해당없음'),
        ('under_17', '17성 이하'),
        ('up_17', '17성 초과'),
    )

    ABILITY_CHOICES = (
        ('na', '해당없음'),
        ('epic', '에픽'),
        ('unique', '유니크'),
        ('legendary', '레전드리'),
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
        ('warrior', '전사'),
        ('magician', '마법사'),
        ('archer', '궁수'),
        ('thief', '도적'),
        ('pirate', '해적'),
    )

    Armor_CHOICES = (
        ('cap', '모자'),
        ('top', '상의'),
        ('bottom', '하의'),
        ('dress', '한벌옷'),
        ('gloves', '장갑'),
        ('cape', '망토'),
        ('shoes', '신발'),
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
