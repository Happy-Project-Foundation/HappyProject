from django.views.generic import TemplateView


class GalleryView(TemplateView):
    template_name = "gallery/gallery.html"

