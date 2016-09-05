from django.shortcuts import  redirect
from email_service.serializer import EmailServiceSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class EmailServiceDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'email_service/form.html'

    def get(self, request):
        serializer = EmailServiceSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = EmailServiceSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('/')