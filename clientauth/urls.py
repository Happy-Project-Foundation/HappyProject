from django.urls import path
from clientauth.views import auth_view

urlpatterns = [
    path('', auth_view, name="auth_test"),
]
