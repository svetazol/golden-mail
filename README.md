##Virtual environment preparation
for windows (used python 3.5.2)
```
cd <projects_home>  #D:\PythonPrograms\django_emailing
cd django_emailing
virtualenv django_emailing_env
django_emailing_env\Scripts\activate.bat

pip install -r requirements.txt
```
##drf-extensions
django_emailing_env/Lib/site-packages/rest_framework_extensions/compat.py line:22
have to be changed on "from django.conf.urls import url, include" without import patterns (it is removed in Django 1.10)

##RabbitMQ web interface
```
rabbitmq-plugins enable rabbitmq_management
http://localhost:15672/
```

##Celery
### Starting the worker process
```
celery -A golden_mail worker -l info
```
### monitoring
```
celery flower -A golden_mail
http://localhost:5555
```

