from django.shortcuts import render

# Create your views here.
def index(request):
    """A view to test our initial application version."""
    # We can actually create a context locally for the rendered view
    context = {
        'movies': [
            'gladiator',
            'top gun',
            'casino',
        ]
    }
    return render(request, 'movies/index.html', context)


def about(request):
    """A function rendering a page describing our movies application."""
    return render(request, 'movies/about.html', {})

# To identify a template, use the path
# `<app_name>/templates/<app_name>/<html_filename>
