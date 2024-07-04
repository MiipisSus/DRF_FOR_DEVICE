from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import celery_tester


urlpatterns = [
    path('auth/', obtain_auth_token, name='api_token_auth'),
    path('task/add/', celery_tester, name='task_add')
]
