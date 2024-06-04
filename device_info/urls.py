from django.urls import path

from . import views

urlpatterns = [
    path('video/', views.GetMultimediaValueVideoView.as_view(), name="get_multimedia_value_video"),
    path('video/update/', views.SetMultimediaValueVideoView.as_view(), name="set_multimedia_value_video"),
    path('image/', views.GetMultimediaValueImageView.as_view(), name="get_multimedia_value_image"),
    path('image/update/', views.GetMultimediaValueImageView.as_view(), name="set_multimedia_value_image")
]
