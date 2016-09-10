from django.contrib.auth.models import User
from django.db import models


class EmailRequest(models.Model):
    owner = models.ForeignKey(User)
    sending_dttm = models.DateTimeField()
    email = models.EmailField()
    message = models.TextField()
    status = models.CharField(max_length=16,blank=True)

    class Meta:
        db_table = 'email_request'