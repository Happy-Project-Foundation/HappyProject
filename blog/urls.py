from django.urls import path

from .views import BlogView

app_name = "blog"
urlpatterns = [
    path('<uuid:pk>', BlogView.as_view(), name="index"),
]
