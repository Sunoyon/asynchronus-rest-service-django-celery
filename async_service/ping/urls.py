from django.conf.urls import url

import views

urlpatterns = [
    # ex: /ping/
    url(r'^$', views.index, name='index'),
]

    
