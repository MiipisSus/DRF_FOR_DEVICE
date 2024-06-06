from django.urls import path

from . import views

urlpatterns = [
    path('info/', views.GetStorageInfoView.as_view(), name='get_storage_info')
]