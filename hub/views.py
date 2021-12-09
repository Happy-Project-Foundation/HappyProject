from django.http.response import HttpResponseServerError
from django.views.generic import ListView

from .models import Resource
from blog.models import Blog


class HubView(ListView):
    template_name = "hub/hub.html"
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
        context["user"] = "student"
        context["page_title"] = "Happy Hub | Happy Project 😊"
        
        context["types"] = [type[1] for type in Resource._types]
        context["subjects"] = [subject[1] for subject in Resource._subjects]

        # trending blogs construction
        context["blogs"] = Blog.objects.all().order_by("title")[:8]

        return context
    
