from django.urls import path

from blog.views import blog_view

urlpatterns = [
    path('', blog_view, name="blog_test"),
]
