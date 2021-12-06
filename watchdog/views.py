from django.http import HttpResponse


def api_text_view(request):
    return HttpResponse("Hello, world. You're at the api of happy project index.")
