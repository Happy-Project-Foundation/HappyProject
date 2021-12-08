from django.urls import path

from .views import HubView

app_name = "hub"
urlpatterns = [
    path('', HubView.as_view(), name="index")
]
