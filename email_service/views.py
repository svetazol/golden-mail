from time import sleep

from django.http import Http404
from rest_framework import permissions
from rest_framework_extensions.cache.decorators import cache_response
from email_service.models import EmailRequest
from email_service.permissions import IsOwnerOrReadOnly
from email_service.serializer import EmailRequestSerializer, MessageSerializer
from email_service.tasks import send_email
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class EmailRequestDetail(APIView):
    def get_object(self, pk):
        try:
            return EmailRequest.objects.get(pk=pk)
        except EmailRequest.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        email_request = self.get_object(pk)
        serializer = EmailRequestSerializer(email_request)
        return Response(serializer.data)


class EmailRequestList(APIView):
    # fixme: IsOwnerOrReadOnly, check_object_permissions is not called for APIView (but for GenericAPIView), add filter by user to get method?
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)

    @cache_response(cache_errors=False, timeout=15 * 60)
    def get(self, request):
        email_requests = EmailRequest.objects.all()
        sleep(20)
        serializer = EmailRequestSerializer(email_requests, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.copy()
        data['owner'] = request.user.id
        serializer = EmailRequestSerializer(data=data)
        if serializer.is_valid():
            email_request_obj = serializer.save(status='ожидает')
            send_email.apply_async((email_request_obj.message, email_request_obj.email, email_request_obj.pk),
                                   eta=email_request_obj.sending_dttm)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageList(APIView):
    # fixme: IsOwnerOrReadOnly, check_object_permissions is not called for APIView (but for GenericAPIView), add filter by user to get method?
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)

    def get(self, request):
        email_requests = EmailRequest.objects.all()
        status = self.request.query_params.get('status', None)
        if status is not None:
            email_requests = email_requests.filter(status=status)
        serializer = MessageSerializer(email_requests, many=True)
        return Response(serializer.data)
