# asynchronus-rest-service-django-celery


## Introduction

This is an example of asynchronus microservice using django and celery. Redis is used as task broker. Celery worker-node acts as a consumer of the task broker and runs the tasks. Therefore no callback scenario is available in this approach.


### Prerequisite

*   Django==1.9.1
*   Celery==3.1.19 (Cipater)
*   Redis==2.10.6

Run
	
	$ pip install async_service/requirements.pip 

### How to run
To migrate for django and run the redis server

	$ cd async_service
	$ python manage.py makemigrations
	$ python manage.py migrate
	$ redis-server &
	
To run django server

	$ python manage.py runserver
	$ python manage.py createsuperuser
	
To run the celeryd using django manage.py

	$ python manage.py celeryd -l info
	
Curl to the endpoint

	$ curl -i http://localhost:8000/ping/
	
To see the list of tasks in Redis

	$ redis-cli
	$ 127.0.0.1:6379> keys *

To resolve errors that might pop up

	* To resolve "django.templatetags.future" error in >=1.9 Django versions, remove "/lib/python2.7/dist-packages/django/templatetags/future.py" and "/lib/python2.7/dist-packages/django/templatetags/future.pyc" files situated in "/usr/local" or "~/.local" directories.
	* To resolve "AttributeError: 'unicode' object has no attribute 'iteritems" in "/site-packages/redis/_compat.py", install redis==2.0.1 instead of redis==3.0.1.
		$ pip uninstall redis
		$ pip install redis==2.10.6
	* Install django-celery if unidentified celery package error is coming up after "pip install 
		$ pip install django-celery
