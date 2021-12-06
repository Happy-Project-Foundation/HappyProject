from django.http import HttpResponse


def blog_view(request):
    return HttpResponse("this is a blog post if any.")
