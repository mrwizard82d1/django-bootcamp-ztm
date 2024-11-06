from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

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
