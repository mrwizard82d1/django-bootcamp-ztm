Must change the `index` view
- Add `from .models import JobPosting`
- Query `JobPosting.objects.all()`
- Print result of query to console

After verifying printing all job postings, use `filter()` method to look at **active** job postings
- `JobPosting.objects.filter(is_active=True)`

We have now verified our data and filtering is `is_active`
- Time to incorporate this information into our template

