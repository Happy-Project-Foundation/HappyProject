from django.http.response import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Resource
from blog.models import Blog

from watchdog.models import (
    STUDENT, TEACHER, DONOR, DEV, GAZER, ADMIN,
)


# index view ----------------------------------------------
@login_required(login_url='clientauth:login')
def hub_index(req):
    if req.user.role == STUDENT:
        return HttpResponseRedirect(redirect_to=reverse('hub:student'))

    elif req.user.role == TEACHER:
        return HttpResponseRedirect(redirect_to=reverse('hub:teacher'))

    elif req.user.role == DONOR:
        pass
    elif req.user.role == DEV:
        pass
    elif req.user.role == GAZER:
        pass
    elif req.user.role == ADMIN:
        return HttpResponseRedirect(redirect_to=reverse('home:index'))

    else:
        return Http404()


# noinspection PyShadowingBuiltins,PyProtectedMember
@login_required(login_url='clientauth:login')
def student(req):
    context = dict()
    context["page_title"] = "Happy Hub | Happy Project 😊"
    context["types"] = [type[1] for type in Resource._types]
    context["subjects"] = [subject[1] for subject in Resource._subjects]
    context["blogs"] = Blog.objects.all().order_by("title")[:8]

    return render(
        request=req, template_name="hub/student_hub.html"
    )

# class StudentHubView(LoginRequiredMixin ,ListView):
#     template_name = "hub/studet_hub.html"
#     paginate_by = 15
#     model = Resource
#     ordering = ["title"]
#
#
#     def get_queryset(self):
#         try:
#             keys = self.request.GET.keys()
#             if "type" in keys:
#                 queryset = Resource.objects.filter(
#                     type__icontains=self.request.GET["type"]).order_by("title")
#             elif "subject" in keys:
#                 queryset = Resource.objects.filter(
#                     subject__icontains=self.request.GET["subject"]).order_by("title")
#             elif "search" in keys:
#                 # TODO: search within description also
#                 queryset = Resource.objects.filter(
#                     title__icontains=self.request.GET["search"]).order_by("title")
#             else:
#                 queryset = super().get_queryset().order_by("title")
#
#         except:
#             raise HttpResponseServerError()
#
#         else:
#             return queryset
#
#
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         # NOTE: Test var.
#         context["page_title"] = "Happy Hub | Happy Project 😊"
#
#         context["types"] = [type[1] for type in Resource._types]
#         context["subjects"] = [subject[1] for subject in Resource._subjects]
#
#         # trending blogs construction
#         context["blogs"] = Blog.objects.all().order_by("title")[:8]
#
#
#
#         return context
