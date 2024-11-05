from django.shortcuts import render
from django.views.generic import ListView

from .models import Profile, Link

# Create your views here.
class LinkListView(ListView):
    """Create a `ListView` child to view all links."""
    model = Link
    # Will automatically look for a template class `link_list.html`
