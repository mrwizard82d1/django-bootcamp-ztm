from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    """The home page template."""
    template_name = 'trip/index.html'
