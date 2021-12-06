from django.http import HttpResponse


def gallery_view(request):
    return HttpResponse("this is for gallery.")
