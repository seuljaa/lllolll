from django.contrib import admin

# Register your models here.
from accounts.models import User
from deal.models import DealItems
from job.models import Post_job

admin.site.register(User)
admin.site.register(DealItems)
admin.site.register(Post_job)
