from django.db import models
from accounts.models import User
from config import settings

# Create your models here.


class Photo_post(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    create_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)
    imgfile = models.ImageField(null=True, upload_to="", blank=True)
    content = models.TextField()
    likes_user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,  # this is preferred than just 'User'
        blank=True,  # blank is allowed
        related_name='likes_user'
    )  # likes_user field

    def count_likes_user(self):  # total likes_user
        return self.likes_user.count()