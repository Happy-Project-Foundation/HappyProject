"""happy_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('home.urls')),
    path('clientauth/', include('clientauth.urls')),
    path('blog/', include('blog.urls')),
    path('gallery/', include('gallery.urls')),
    path('hub/', include('hub.urls')),
    path('api/', include('watchdog.urls')),
    path('test-admin/', auth_views.LoginView.as_view(
        template_name='clientauth/login.html',
        next_page="/guard/",
        redirect_authenticated_user=True
    ), name="admin"),
    path('guard/', admin.site.urls),
]
