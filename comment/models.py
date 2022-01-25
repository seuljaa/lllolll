from django.db import models
from accounts.models import User
from deal.models import DealItems
from photo.models import Photo_post
from job.models import Post_job

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True, auto_now=True)
    deal_items = models.ForeignKey(DealItems, null=True, blank=True, on_delete=models.CASCADE)
    photo_post = models.ForeignKey(Photo_post, null=True, blank=True, on_delete=models.CASCADE)
    job_post = models.ForeignKey(Post_job, null=True, blank=True, on_delete=models.CASCADE)