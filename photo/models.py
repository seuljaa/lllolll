import os

from django.db import models
from accounts.models import User
from config import settings


# Create your models here.

class Photo_post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)
    imgfile = models.ImageField(null=True, upload_to="", blank=True)
    content = models.TextField()
    like_count = models.PositiveIntegerField(default=0)
    likes_user = models.ManyToManyField(
        User,  # this is preferred than just 'User'
        blank=True,  # blank is allowed
        related_name='likes_user'
    )

    def count_likes_user(self):  # total likes_user
        return self.likes_user.count()


    def delete(self, *args, **kargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.imgfile.name))
        super(Photo_post, self).delete(*args, **kargs)