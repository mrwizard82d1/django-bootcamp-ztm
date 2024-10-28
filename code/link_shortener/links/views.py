from django.shortcuts import render

from .models import Link

# Create your views here.

def index(request):
    """Return the `index` page."""

    # We want to fill the context with all the links currently read
    # from the database
    links = Link.objects.all()
    context = {'links': links}

    # Render the request using the specified template and context
    return render(request, 'links/index.html', context)
