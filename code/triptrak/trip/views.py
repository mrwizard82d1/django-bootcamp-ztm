from django.shortcuts import render
from django.views.generic import TemplateView

# Trip for now; Note for later.
from .models import Trip, Note

# Create your views here.
class HomeView(TemplateView):
    """The home page template."""
    template_name = 'trip/index.html'


def trips_list(request):
    """View the list of all trips"""
    trips = Trip.objects.filter(owner=request.user)
    context = {'trips': trips}

    return render(request, 'trip/trip_list.html', context)
