from django.views.generic import ListView

from hub.models import Resource


class HubView(ListView):
    template_name = "hub/hub.html"
    paginate_by = 15
    model = Resource
    ordering = ["title"]


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # NOTE: Test var.
        context["user"] = "student"
        context["page_title"] = "Birnadin Erick's hub | Happy Project 😊"
        context["types"] = [type[1] for type in Resource._types]
        context["subjects"] = [subject[1] for subject in Resource._subjects]

        return context
    
