from django.urls import path
from clientauth.views import ClientLoginView, join

app_name = "clientauth"
urlpatterns = [
    path('login', ClientLoginView.as_view(), name="login"),
    path('join', join, name="join"),
]
