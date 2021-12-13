from django.urls import path

from .views import SoonView, stray_user

app_name = "api"
urlpatterns = [
    path('soon', SoonView.as_view(), name='soon'),
    path('stray', stray_user, name='stray')
]
