from django.conf.urls import url
from email_service.views import EmailRequestDetail, EmailRequestList, MessageList

urlpatterns = [
    url(r'^email_requests/$', EmailRequestList.as_view(), name='email_requests'),
    url(r'^email_requests/(?P<pk>[0-9]+)/$', EmailRequestDetail.as_view()),
    url(r'^messages/$', MessageList.as_view()),
]