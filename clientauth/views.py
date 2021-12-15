from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render
from django.urls import reverse_lazy

from hub.models import Student
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
def onboard_student(req):
    if req.user.is_authenticated and req.user.is_verified and (req.user.role != 1):
        return HttpResponseRedirect(
            reverse_lazy('api:stray')
        )

    if req.method == "POST":
        try:
            # parse user inputs
            country = str(req.POST["country"]).lower()
            lang = req.POST["lang"].lower()
            motto = req.POST["motto"]
            school = req.POST["school"].title()
            age = int(req.POST["age"])
            resources = parse_text_area(req.POST["resources"])
            subjects = parse_text_area(req.POST["subjects"])

            # create a student model
            student = Student(
                student=req.user,
                subjects=subjects,
                resources=resources,
                school=school,
                country=country,
                motto=motto,
                language=lang,
                age=age
            )

            student.student.is_verified = True
            print(student.student.is_verified)

            # commit the change
            student.student.save()
            student.save()

        except Exception as e:
            print(e.__str__())
            return HttpResponseServerError()
        else:
            return HttpResponseRedirect(
                reverse_lazy("hub:student")
            )
    else:
        return render(
            request=req,
            template_name="clientauth/onboarding/student.html"
        )


# utils --------------------------------------------------------------------------------------------
def parse_text_area(arg: str) -> str:
    return ",".join([
        r.lower().strip(" ") for r in str(arg).split(",")
        if (not r.isdigit())
    ])
