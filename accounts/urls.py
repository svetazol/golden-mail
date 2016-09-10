from accounts.views import register, UserList
from django.conf.urls import url
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(
        r'^login/$', login, name='login',
        kwargs={'template_name': 'accounts/login.html'}
    ),
    url(
        r'^logout/$', logout, name='logout',
        kwargs={'next_page': '/'}
    ),
    url('^register/', register, name='register'),
    url(r'^users', UserList.as_view())
]