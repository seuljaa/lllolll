from django.contrib import admin

# Register your models here.
from accounts.models import User
from deal.models import DealItems

admin.site.register(User)
admin.site.register(DealItems)