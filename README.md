##Virtual environment preparation
for windows (used python 3.5.2)
```
cd <projects_home>  #D:\PythonPrograms\django_emailing
cd django_emailing
virtualenv django_emailing_env
django_emailing_env\Scripts\activate.bat

pip install -r requirements.txt
```

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
```