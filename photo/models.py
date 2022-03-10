import os

from django.db import models
from accounts.models import User
from config import settings


# Create your models here.

class Photo_post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)
    content = models.TextField()
    like_count = models.PositiveIntegerField(default=0)
    likes_user = models.ManyToManyField(
        User,  # this is preferred than just 'User'
        blank=True,  # blank is allowed
        related_name='likes_user'
    )
    ct_id = models.PositiveIntegerField('content_type_id', default=11)

    def count_likes_user(self):  # total likes_user
        return self.likes_user.count()



class Photo_Image(models.Model):

    post = models.ForeignKey(Photo_post, on_delete=models.CASCADE)
    imgfile = models.ImageField(null=False, upload_to="photo", blank=False)

    def delete(self, *args, **kargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.imgfile.name))
        super(Photo_post, self).delete(*args, **kargs)

class Main_Image(models.Model):

    imgfile = models.ImageField(null=False, upload_to="photo", blank=False)

    def delete(self, *args, **kargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.imgfile.name))

class Photo_like(models.Model):
    post = models.ForeignKey(Photo_post, on_delete=models.CASCADE)
    like_count = models.PositiveIntegerField(default=0)
    likes_user = models.ManyToManyField(
        User,  # this is preferred than just 'User'
        blank=True,  # blank is allowed
    )
    ct_id = models.PositiveIntegerField('content_type_id', default=12)

    def count_likes_user(self):  # total likes_user
        return self.likes_user.count()