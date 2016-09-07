from django.http import Http404
from django.shortcuts import redirect
from email_service.models import EmailService
from email_service.serializer import EmailServiceSerializer
from email_service.tasks import send_email
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class EmailServiceDetail(APIView):
    def get_object(self, pk):
        try:
            return EmailService.objects.get(pk=pk)
        except EmailService.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        email_service = self.get_object(pk)
        serializer = EmailServiceSerializer(email_service)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmailServiceSerializer(data=request.data)
        if serializer.is_valid():
            email_service_obj = serializer.save()
            send_email.apply_async((email_service_obj.message, email_service_obj.email),
                                   eta=email_service_obj.sending_dttm)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)