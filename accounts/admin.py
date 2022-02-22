from django.contrib import admin

# Register your models here.
from accounts.models import User
from deal.models import DealItems
from job.models import Post_job
from photo.models import Photo_post
from comment.models import Comment

admin.site.register(User)
admin.site.register(DealItems)
admin.site.register(Post_job)
admin.site.register(Photo_post)
admin.site.register(Comment)

