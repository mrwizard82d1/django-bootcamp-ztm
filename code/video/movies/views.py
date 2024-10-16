from django.shortcuts import render

# Create your views here.
def index(request):
    """A view to test our initial application version."""
    # The third argument to `render` is called the "context."
    # The context is modeled by a dictionary containing the replaceable
    # parameters for data to be substituted into our template.
    return render(request, 'movies/index.html', {})


def about(request):
    """A describing our movies application."""
    return render(request, 'movies/about.html', {})

# To identify a template, use the path
# `<app_name>/templates/<app_name>/<html_filename>
