from django.urls import path
from clientauth.views import auth_view

app_name = "clientauth"
urlpatterns = [
    path('', auth_view, name="index"),
]
