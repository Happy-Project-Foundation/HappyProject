from django.views.generic import TemplateView


class HubView(TemplateView):
    template_name = "hub/hub.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # NOTE: Test var.
        context["user"] = "student"
        return context
    
