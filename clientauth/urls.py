from django.urls import path
from clientauth.views import LoginView, RegisterView

app_name = "clientauth"
urlpatterns = [
    path('login', LoginView.as_view(), name="login"),
    path('join', RegisterView.as_view(), name="join"),
]
