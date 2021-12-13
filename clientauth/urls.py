from django.urls import path

from clientauth.views import (
    ClientLoginView, join, PasswordResetActionView,
    PasswordResetSuccessView, PasswordResetRequestedView,
    ForgotPasswordView, StudentOnboardingView
)

from django.contrib.auth.views import LogoutView

app_name = "clientauth"
urlpatterns = [
    # commons
    path('login', ClientLoginView.as_view(), name="login"),
    path('join', join, name="join"),
    path('logout', LogoutView.as_view(), name="logout"),

    # password reset
    path('forgot_password', ForgotPasswordView.as_view(), name="forgot_password"),
    path('password_reset_requested', PasswordResetRequestedView.as_view(), name="password_reset_requested"),
    path('password_reset_action/<uidb64>/<token>/', PasswordResetActionView.as_view(), name="password_reset_action"),
    path('password_reset_success', PasswordResetSuccessView.as_view(), name="password_reset_success"),

    # onboardings
    path('onboard/student', StudentOnboardingView.as_view(), name="onboard_student")
]
