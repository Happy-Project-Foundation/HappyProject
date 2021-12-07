from django.urls import path

from .views import GalleryView



app_name = "gallery"
urlpatterns = [
    path('', GalleryView.as_view(), name="index")
]
