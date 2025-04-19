from django.http import HttpResponse


def about_page(request):
    return HttpResponse("Hello World")