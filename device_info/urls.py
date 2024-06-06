from django.urls import path

from . import views

urlpatterns = [
    path('basic/', views.GetBasicDeviceInfo.as_view(), name="get_basic_device_info"),
    path('basic/update/', views.SetBasicDeviceInfo.as_view(), name="set_basic_device_info"),
    path('network/', views.GetNetworkInfo.as_view(), name="get_network_info"),
    path('network/update', views.SetNetworkInfo.as_view(), name="set_network_info"),
    path('video/', views.GetMultimediaValueVideoView.as_view(), name="get_multimedia_value_video"),
    path('video/update/', views.SetMultimediaValueVideoView.as_view(), name="set_multimedia_value_video"),
    path('image/', views.GetMultimediaValueImageView.as_view(), name="get_multimedia_value_image"),
    path('image/update/', views.SetMultimediaValueImageView.as_view(), name="set_multimedia_value_image"),
    path('osd/', views.GetOSDInfo.as_view(), name="get_osd_info"),
    path('osd/update/', views.SetOSDInfo.as_view(), name="set_osd_info"),
]
