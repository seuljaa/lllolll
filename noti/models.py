from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.

class Noti(models.Model):
    to_user = models.ForeignKey("accounts.User", on_delete=models.DO_NOTHING)
    content_type = models.ForeignKey(ContentType, related_name="content_type_noti", on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField('관련 데이터 번호')
    content_object = GenericForeignKey('content_type', 'object_id')
    is_viewed = models.BooleanField('읽음여부', default=False)

    @property
    def click(self):
        self.is_viewed = True
        self.save()

class Noti_item(models.Model):
    noti = models.ForeignKey(Noti, null=True, blank=True, on_delete=models.CASCADE)
    from_user = models.ForeignKey("accounts.User", on_delete=models.DO_NOTHING)
    content_type = models.ForeignKey(ContentType, related_name="content_type_noti_item", on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField('관련 데이터 번호')
    content_object = GenericForeignKey('content_type', 'object_id')
