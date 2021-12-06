from django.urls import path

from hub.views import hub_view

urlpatterns = [
    path('', hub_view)
]
