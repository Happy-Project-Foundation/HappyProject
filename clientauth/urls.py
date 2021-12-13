from django.urls import path

from clientauth.views import (
    ClientLoginView, join, PasswordResetActionView,
    PasswordResetSuccessView, PasswordResetRequestedView,
    ForgotPasswordView
)

from django.contrib.auth.views import LogoutView

app_name = "clientauth"
urlpatterns = [
    path('login', ClientLoginView.as_view(), name="login"),
    path('join', join, name="join"),
    path('forgot_password', ForgotPasswordView.as_view(), name="forgot_password"),
    path('password_reset_requested', PasswordResetRequestedView.as_view(), name="password_reset_requested"),
    path('password_reset_action/<uidb64>/<token>/', PasswordResetActionView.as_view(), name="password_reset_action"),
    path('password_reset_success', PasswordResetSuccessView.as_view(), name="password_reset_success"),
    path('logout', LogoutView.as_view(), name="logout"),
]
