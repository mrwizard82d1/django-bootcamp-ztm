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
    # The video simply changed the `all()` predicate on `Trip.object1 to
    # call to filter below. This change, when run in Django 5.x causes
    # the code to break with a `TypeError` indicating that the code
    # "...the field 'id' expected a number but got....". The following
    # code with the `is_authenticated` "gate" works with Django 5.x.
    if request.user.is_authenticated:
        trips = Trip.objects.filter(owner=request.user)
        context = {'trips': trips}
    else:
        context = {}

    return render(request, 'trip/trip_list.html', context)
