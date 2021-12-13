from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from watchdog.models import HappyPerson


class ClientLoginView(LoginView):
    template_name = "clientauth/login.html"


class PasswordResetSuccessView(auth_views.PasswordResetCompleteView):
    template_name = "clientauth/password_reset_complete.html"


class PasswordResetActionView(auth_views.PasswordResetConfirmView):
    template_name = "clientauth/password_reset_confirm.html"
    success_url = reverse_lazy("clientauth:password_reset_success")


class PasswordResetRequestedView(auth_views.PasswordResetDoneView):
    template_name = "clientauth/password_reset_done.html"


class ForgotPasswordView(auth_views.PasswordResetView):
    email_template_name = "clientauth/password_reset_email.html"
    template_name = "clientauth/password_reset_form.html"
    success_url = reverse_lazy("clientauth:password_reset_requested")


def join(req):
    if req.user.is_authenticated:
        return HttpResponseRedirect(
            reverse_lazy('clientauth:login')
        )

    if req.method == "POST":

        email = req.POST['email']
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        role = int(req.POST['rad'][0])
        passwd = req.POST['passwd']

        try:
            new_person = HappyPerson.objects.create_user(
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=passwd
            )
            new_person.role = role
            if role != 1:
                new_person.is_staff = True
                new_person.is_active = False
            new_person.save()
        except:
            return HttpResponseServerError()
        else:
            return HttpResponseRedirect(
                reverse_lazy('clientauth:login')
            )

    else:
        return render(
            request=req,
            template_name="clientauth/join.html"
        )


# onboarding views -----------------------------------------------------------------------------------------------------
class StudentOnboardingView(TemplateView):
    template_name = 'clientauth/onboarding/student.html'
