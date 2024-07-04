from django.shortcuts import render
from django.http import HttpResponse

from .tasks import add

def celery_tester(request):
    result = add.delay(4, 6)
    return HttpResponse(f'res: {result.get()}')