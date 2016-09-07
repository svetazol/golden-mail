"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from accounts import views as accounts_views
from email_service import views as email_service_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^email_service/$', email_service_views.EmailServiceDetail.as_view(), name='email_service'),
    url(r'^email_service_form/', TemplateView.as_view(template_name="email_service/form.html"),
        name='email_service_form'),
    url(r'^$', login_required(TemplateView.as_view(template_name='index.html'))),
    # fixme how to manage api/ ?
    url(r'^api/users', accounts_views.UserList.as_view())
]
