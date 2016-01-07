from django.shortcuts import render
from django.http import HttpResponse
from ping.tasks import async_task


# Create your views here.
def index(request):
    async_task.delay()
    return HttpResponse("pong", content_type='application/plain')