# myapp/routing.py
from django.urls import re_path
from .consumers import TestConsumer

websocket_urlpatterns = [
    re_path(r'ws/some_path/$', TestConsumer.as_asgi()),
]