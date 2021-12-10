from django.views.generic import TemplateView
from django.contrib.auth.models import User

class LoginView(TemplateView):
    template_name = "clientauth/login.html"


class RegisterView(TemplateView):
    template_name = "clientauth/register.html"


def student_join(req):
    if req.method == "POST":
        username = req[""]
