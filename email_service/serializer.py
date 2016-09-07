from email_service.models import EmailService
from rest_framework import serializers


class EmailServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailService
        fields = ('sending_dttm', 'email', 'message', 'owner')