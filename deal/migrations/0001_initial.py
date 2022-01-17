# Generated by Django 4.0.1 on 2022-01-17 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DealItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100, verbose_name='제목')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='갱신날짜')),
                ('server', models.CharField(choices=[('scania', '스카니아'), ('bera', '베라'), ('luna', '루나'), ('zenith', '제니스'), ('croa', '크로아'), ('union', '유니온'), ('elysium', '엘리시움'), ('enosis', '이노시스'), ('red', '레드'), ('aurora', '오로라'), ('arcane', '아케인'), ('nova', '노바')], max_length=10, verbose_name='서버')),
                ('group', models.CharField(choices=[('warrior', '전사'), ('magician', '마법사'), ('archer', '궁수'), ('thief', '도적'), ('pirate', '해적')], max_length=10, verbose_name='직업군')),
                ('part', models.CharField(choices=[('cap', '모자'), ('top', '상의'), ('bottom', '하의'), ('dress', '한벌옷'), ('gloves', '장갑'), ('cape', '망토'), ('shoes', '신발')], max_length=10, verbose_name='부위')),
                ('price', models.PositiveIntegerField(verbose_name='가격')),
                ('price_kind', models.BooleanField(default=True, verbose_name='억/엄')),
                ('star_force', models.CharField(choices=[('na', '해당없음'), ('under_17', '17성 이하'), ('up_17', '17성 초과')], max_length=9, verbose_name='스타포스')),
                ('ability_1', models.CharField(choices=[('na', '해당없음'), ('epic', '에픽'), ('unique', '유니크'), ('legendary', '레전드리')], max_length=9, verbose_name='윗잠')),
                ('ability_2', models.CharField(choices=[('na', '해당없음'), ('epic', '에픽'), ('unique', '유니크'), ('legendary', '레전드리')], max_length=9, verbose_name='아랫잠')),
                ('content', models.TextField()),
                ('sale_buy', models.BooleanField(default=True, verbose_name='삼/팜')),
                ('is_complete', models.BooleanField(default=False, verbose_name='완료여부')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
