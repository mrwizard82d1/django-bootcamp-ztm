from django.shortcuts import render, HttpResponse

from .models import JobPosting

# Create your views here.
def index(request):
    """Return the index page of this application."""

    active_postings = JobPosting.objects.filter(is_active=True)
    context = {'job_postings': active_postings}

    return render(request, 'job_board/index.html', context)

def job_detail(request, pk):
    """Return the job details page of this application.

    request - The HTTPRequest for this view.
    pk - The value (ie. "primary key") identifying the job whose details I display.
    """

    job_posting = JobPosting.objects.get(pk=pk)
    context = {'posting': job_posting}

    print(context)
    return render(request, 'job_board/detail.html', context)
