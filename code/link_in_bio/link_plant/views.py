from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Profile, Link

# Create your views here.
class LinkListView(ListView):
    """Create a `ListView` child to view all links."""
    model = Link
    # Will automatically look for a template class `link_list.html`


class LinkCreateView(CreateView):
    """Creat a view to create new links."""
    # What `CreateView` supports
    # - Create `forms.py` file and form
    # - Check if this was a post or a get request
    # - Return an empty form or save the form data

    model = Link
    # Puts **all** `Link` field into the form
    fields = "__all__"
    success_url = reverse_lazy('link-list')
    # By default
    # - Creates a template model_form; i.e., `link_form.html`


class LinkUpdateView(UpdateView):
    """Update a existing link."""
    # With a function view
    # Create a form
    # Check if get or put request
    # Either render form or update and save
    # `UpdateView` encapsulates this pattern
    model = Link
    fields = ['text', 'url']
    success_url = reverse_lazy('link-list')
    # This class uses the **same** template as the `LinkCreateView`


class LinkDeleteView(DeleteView):
    """Delete an existing link."""
    # If using a function view
    # - Take in an id (primary key) of an object (to delete)
    # - Query the database for that object
    # - If it exists, delete the object
    # - Either return some template or forward the user to some URL
    model = Link

    # If successful, return to the `link-list` URL
    success_url = reverse_lazy('link-list')

    # By default, this implementation will provide
    # - A form to submit in order to delete the item
    # -
