from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    """Home view."""
    return HttpResponse("Hello, Django my-app world!")


def about(request):
    """About view."""
    return HttpResponse("About Me")


def hello(request, first_name):
    """Return a friendly greeting of `first_name`."""
    return HttpResponse(f"Hello, {first_name}")
