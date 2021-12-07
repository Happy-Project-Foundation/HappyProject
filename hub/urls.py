from django.urls import path

from hub.views import hub_view

app_name = "hub"
urlpatterns = [
    path('', hub_view, name="index")
]
