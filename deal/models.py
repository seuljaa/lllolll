from django.db import models
from accounts.models import User

# Create your models here.

class DealItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject = models.CharField('제목', max_length=100)
    create_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)
    server = models.CharField('서버', max_length=10)
    category = models.BooleanField('장비/기타', default=True)
    group = models.CharField('직업군', max_length=10)
    kind = models.CharField('종류', max_length=10)
    part = models.CharField('부위', max_length=10)
    price = models.PositiveIntegerField('가격')
    price_kind = models.BooleanField('억/엄', default=True)
    star_force = models.CharField('스타포스', max_length=9, null=True)
    ability_1 = models.CharField('윗잠', max_length=9, null=True)
    ability_2 = models.CharField('아랫잠', max_length=9, null=True)
    content = models.TextField()
    sale_buy = models.BooleanField('삼/팜', default=True)
    is_complete = models.BooleanField('완료여부', default=False)
    ct_id = models.PositiveIntegerField('content_type_id', default=8)

class Group(models.Model):
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

    ARMOR_CHOICES = (
        ('모자', '모자'),
        ('상의', '상의'),
        ('하의', '하의'),
        ('한벌옷', '한벌옷'),
        ('장갑', '장갑'),
        ('망토', '망토'),
        ('신발', '신발'),
    )

    ACCESSORY_CHOICES = (
        ('얼굴장식', '얼굴장식'),
        ('눈장식', '눈장식'),
        ('귀고리', '귀고리'),
        ('어깨장식', '어깨장식'),
        ('반지', '반지'),
        ('펜던트', '펜던트'),
        ('벨트', '벨트'),
        ('포켓아이템', '포켓아이템'),
    )

    WEAPON_CHOICES = (
        ('주무기', '주무기'),
        ('보조무기', '보조무기'),
    )

    KIND_CHOICES = (
        ('방어구', '방어구'),
        ('장신구', '장신구'),
        ('무기', '무기'),
        ('캐시', '캐시'),
        ('교불', '교불'),
    )
    kind = models.CharField('종류', max_length=10, choices=KIND_CHOICES)
    part_armor = models.CharField('부위_방어구', max_length=10, choices=ARMOR_CHOICES, null=True)
    part_accessory = models.CharField('부위_장신구', max_length=10, choices=ACCESSORY_CHOICES, null=True)
    part_weapon = models.CharField('부위_무기', max_length=10, choices=WEAPON_CHOICES, null=True)
    star_force = models.CharField('스타포스', max_length=9, choices=STAR_FORCE_CHOICES, null=True)
    ability_1 = models.CharField('윗잠', max_length=9, choices=ABILITY_CHOICES, null=True)
    ability_2 = models.CharField('아랫잠', max_length=9, choices=ABILITY_CHOICES, null=True)