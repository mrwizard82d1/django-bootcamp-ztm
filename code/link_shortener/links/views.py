from django.shortcuts import render, get_object_or_404, redirect

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


def root_link(request, link_slug):
    """Navigate to the 'root_link' for a shortened link.

    Users goes to 'google' on our site then they navigate
    to www.google.com; that is, click on the short link
    and navigate to the stored, long link.

    request - A model of the HTTP request.
    link_slug - The short link to be "expanded" when clicked.
    """
    link = get_object_or_404(Link, slug=link_slug)
    # increments the click count of the retrieved object
    link.click_count()

    # In this scenario, we **do not** want to render anything on
    # our site but instead navigate to a new site.
    return redirect(link.url)


def add_link(request):
    """Render a form that allows the user to add a link."""
    return render(request, 'links/create.html',  {})
