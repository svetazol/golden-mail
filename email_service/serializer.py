from email_service.models import EmailRequest
from rest_framework import serializers


class EmailRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailRequest
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailRequest
        fields = ('message', 'status')