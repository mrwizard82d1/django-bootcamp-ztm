from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

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

class TripCreateView(CreateView):
    """View to create trips."""
    model = Trip
    success_url = reverse_lazy('trip-list')
    # **Do not** include `owner` because we just want to refer to the owner
    # We **do not** want to allow someone to specify a **different**
    # owner for a trip.
    fields = ['city', 'country', 'start_date', 'end_date']

    # Remember to create a template named like "model_form.html"

    # We must create one other piece
    def form_valid(self, form):
        """Validate the form with the previously specified 'fields' but
        **also** we must supply the currently logged in user as the owner."""

        form.instance.owner = self.request.user

        # And then return for additional processing.
        return super().form_valid(form)


