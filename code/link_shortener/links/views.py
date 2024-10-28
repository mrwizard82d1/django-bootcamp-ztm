from django.shortcuts import render

# Create your views here.

def index(request):
    """Return the `index` page."""

    # Render the request using the specified template and context
    return render(request, 'links/index.html', {})
