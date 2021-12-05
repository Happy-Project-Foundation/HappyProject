from django.urls import path

from .views import api_text_view
urlpatterns = [
    path('', api_text_view)
]
