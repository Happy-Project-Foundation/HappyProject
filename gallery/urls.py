from django.urls import path

from gallery.views import gallery_view

app_name = "gallery"
urlpatterns = [
    path('', gallery_view, name="index")
]
