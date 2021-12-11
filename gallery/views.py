from django.views.generic import ListView

from blog.models import Blog


class GalleryView(ListView):
    template_name = "gallery/gallery.html"
    model = Blog
    paginate_by = 10
    ordering = ["title"]

