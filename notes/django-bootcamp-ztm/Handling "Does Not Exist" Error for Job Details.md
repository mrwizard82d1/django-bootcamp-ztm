
Django provides "magic" to handle items **not** in the database
- Replace call to `JobPosting.objects.get()`
- with call to `get_object_or_404(JobPosting, pk=pk, is_active=True)`
	- We request an object from the `JobPosting` table
	- Its primary key (id) is the value, `pk`
	- Additionally, it **must be active**

Run-time operation
- Query `job/1/`
	- Produces "Page not found" page
	- Because job with id, 1, is **not** active
- Query `job/4/`
	- Produces "Page not found" page
	- Because job with id, 4, **does not exist**
- Query `job/2`
	- Produces the details for job with `pk=2`

In our next video
- We will use the "tailwind" CSS package to provide styling to our pages


 