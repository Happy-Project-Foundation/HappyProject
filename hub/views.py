from django.http import HttpResponse


def hub_view(request):
    return HttpResponse("this is a hub for visitors.")