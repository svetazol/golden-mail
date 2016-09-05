from django.contrib.auth.models import User
from django.db import models


class EmailService(models.Model):
    owner = models.ForeignKey(User)
    sending_dttm = models.DateTimeField()
    email = models.EmailField()
    message = models.TextField()
    status = models.CharField(max_length=16)

    class Meta:
        db_table = 'email_service'