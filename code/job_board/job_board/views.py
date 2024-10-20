from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    """Return the index page of this application."""
    return HttpResponse('<h1>Job Board</h1>')