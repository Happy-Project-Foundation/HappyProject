from django.urls import path

from .views import hub_index, student

app_name = "hub"
urlpatterns = [
    path('', hub_index, name="index"),
    path('student/', student, name="student"),
    # path('teacher/', , name="teacher"),
    # path('dev', StudentHubView.as_view()),
    # path('donor', StudentHubView.as_view()),
    # path('gazer', StudentHubView.as_view()),
]
