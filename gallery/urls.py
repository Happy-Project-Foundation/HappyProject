from django.urls import path

from gallery.views import gallery_view

urlpatterns = [
    path('', gallery_view)
]
