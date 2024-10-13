from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    """Home view."""
    return HttpResponse("Hello, Django my-app world!")


def about(request):
    """Home view."""
    return HttpResponse("About app `config`.")
