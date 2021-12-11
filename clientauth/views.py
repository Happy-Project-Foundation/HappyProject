from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render
from django.urls import reverse

from watchdog.models import HappyPerson


class ClientLoginView(LoginView):
    template_name = "clientauth/login.html"
    

def join(req):

    if req.user.is_authenticated:
        return HttpResponseRedirect(
            reverse('hub:index')
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
                new_person.is_active = False
            new_person.save()
        except:
            return HttpResponseServerError()
        else:
            return HttpResponseRedirect(
                reverse('clientauth:login')
            )

    else:
        return render(
            request=req,
            template_name="clientauth/join.html"
        )
