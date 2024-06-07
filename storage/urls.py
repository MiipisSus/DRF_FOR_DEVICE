from django.urls import path

from . import views

urlpatterns = [
    path('info/', views.GetStorageInfoView.as_view(), name='get_storage_info'),
    path('info/update/', views.SetStorageInfoView.as_view(), name='set_storage_info'),
]