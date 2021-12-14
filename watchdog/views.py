from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
from django.views.generic import TemplateView

from .models import (
    STUDENT, TEACHER, DONOR, DEV, GAZER, ADMIN
)


# TODO: change the reverse paths
def stray_user(req):
    if req.user.role == STUDENT:
        if req.user.is_verified:
            return HttpResponseRedirect(
                reverse('hub:student')
            )
        else:
            return HttpResponseRedirect(
                reverse('clientauth:onboard_student')
            )
    elif req.user.role == TEACHER:
        return HttpResponseRedirect(
            reverse('hub:teacher')
        )
    elif req.user.role == DONOR:
        return HttpResponseRedirect(
            reverse('api:soon')
        )
    elif req.user.role == DEV:
        return HttpResponseRedirect(
            reverse('api:soon')
        )
    elif req.user.role == GAZER:
        return HttpResponseRedirect(
            reverse('api:soon')
        )
    elif req.user.role == ADMIN:
        return HttpResponseRedirect(
            reverse('admin')
        )
    else:
        return HttpResponseBadRequest()


class SoonView(TemplateView):
    template_name = "watchdog/comingsoon.html"
