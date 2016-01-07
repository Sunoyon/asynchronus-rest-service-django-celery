'''
Created on Jan 7, 2016

@author: sunoyon
'''

from __future__ import absolute_import
from celery import shared_task, task
import time


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

@task
def async_task():
    print 'async task'
