from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    """A view to test our initial application version."""
    return HttpResponse("My Fav Movies")
