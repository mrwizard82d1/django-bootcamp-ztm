from django.shortcuts import render, HttpResponse

from .models import JobPosting

# Create your views here.
def index(request):
    """Return the index page of this application."""

    active_postings = JobPosting.objects.filter(is_active=True)
    context = {'job_postings': active_postings}

    return render(request, 'job_board/index.html', context)
