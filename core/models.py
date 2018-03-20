from django.db import models


# Create your models here.
class TimeStampMixin(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseModel(TimeStampMixin):
    class Meta:
        abstract = True
