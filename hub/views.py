from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect, HttpResponseServerError
from django.urls import reverse
from django.views.generic import ListView

from blog.models import Blog
from .models import Resource


# index view ----------------------------------------------
@login_required(login_url='clientauth:login')
def hub_index(req):
    # almost unreachable
    return HttpResponseRedirect(reverse('api:stray'))


# noinspection PyShadowingBuiltins,PyProtectedMember
# @login_required(login_url='clientauth:login')
# def student(req):
#     """
#     TODO: integrate pagination
#     """
#     context = dict()
#     context["page_title"] = "Happy Hub | Happy Project 😊"
#     context["types"] = [type[1] for type in Resource._types]
#     context["subjects"] = [subject[1] for subject in Resource._subjects]
#     context["blogs"] = Blog.objects.all().order_by("title")[:8]
#
#     return render(
#         request=req, template_name="hub/student_hub.html"
#     )

class StudentHubView(LoginRequiredMixin, ListView):
    template_name = "hub/student_hub.html"
    paginate_by = 15
    model = Resource
    ordering = ["title"]

    def get_queryset(self):
        try:
            keys = self.request.GET.keys()
            if "type" in keys:
                queryset = Resource.objects.filter(
                    type__icontains=self.request.GET["type"]).order_by("title")
            elif "subject" in keys:
                queryset = Resource.objects.filter(
                    subject__icontains=self.request.GET["subject"]).order_by("title")
            elif "search" in keys:
                # TODO: search within description also
                queryset = Resource.objects.filter(
                    title__icontains=self.request.GET["search"]).order_by("title")
            else:
                queryset = super().get_queryset().order_by("title")

        except:
            raise HttpResponseServerError()

        else:
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # NOTE: Test var.
        context["page_title"] = "Happy Hub | Happy Project 😊"

        context["types"] = [type[1] for type in Resource._types]
        context["subjects"] = [subject[1] for subject in Resource._subjects]

        # trending blogs construction
        context["blogs"] = Blog.objects.all().order_by("title")[:8]

        return context
