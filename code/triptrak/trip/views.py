from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, ListView

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
        **also** we must supply the currently logged-in user as the owner."""

        form.instance.owner = self.request.user

        # And then return for additional processing.
        return super().form_valid(form)


class TripDetailView(DetailView):
    """View the details of a selected trip."""
    model = Trip

    # Currently, we would just get the data stored in the Trip, but we
    # want more information. To repair this issue, we want to update our
    # context variable to include the notes for this trip.
    def get_context_data(self, **kwargs):
        """Get context data for the trip and **also** for its associated notes."""
        context = super().get_context_data(**kwargs)
        trip = context['object']
        # Collect **all** notes associated with this trip
        notes = trip.notes.all()
        context['notes'] = notes
        context['notes_count'] = len(notes)
        return context  ## with trip notes


class NoteDetailView(DetailView):
    """View the details of a selected note."""
    model = Note


class NoteListView(ListView):
    """View all trip notes."""
    model = Note

    def get_queryset(self):
        """Override parent method to get only Notes for currently logged-in user."""
        queryset = Note.objects.filter(trip__owner=self.request.user)
        return queryset


class NoteCreateView(CreateView):
    """Create a note for a trip."""
    model = Note
    success_url = reverse_lazy('note-list')
    fields = '__all__'

    # We only include references to trips for the currently logged in user.
    def get_form(self, **kwargs):
        """Construct the form the current user must fill out **including**
        all the trips of the current user."""

        # Begin by getting the form itself
        form = super(NoteCreateView, self).get_form(**kwargs)

        # Get all the trips for the currently logged in user
        trips = Trip.objects.filter(owner=self.request.user)

        # Add **only** the trips for the current user to the form
        print(f"{form.fields['trip'].queryset=}")
        form.fields['trip'].queryset = trips
        return form

