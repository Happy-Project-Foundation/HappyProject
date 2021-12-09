from django.views.generic.detail import DetailView

from .models import Blog


class BlogView(DetailView):
    template_name = "blog/blog.html"
    model = Blog
    context_object_name = "blog"
