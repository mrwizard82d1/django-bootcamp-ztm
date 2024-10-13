from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    """Home view."""
    return HttpResponse("Hello, Django my-app world!")


def about(request):
    """About view."""
    return HttpResponse("About Me")
