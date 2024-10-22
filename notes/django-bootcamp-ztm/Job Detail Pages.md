Set up the details view so that we can view the details of each job posting

Change `views.py` to render the view for a single job posting
- Create function, `job_detail()`
- In addition to the `request`, this function also takes the key 
	- `pk` for "primary key"
- Get the single job posting with an id of `pk`
- Put the job posting in the `context`
- `render()` the request using the template, `job_board/detail.html`

Add another call to `path`:
- Use `job/<int:pk>/` ("job" followed by the integer primary key) as the path argument
- Use `job_detail` (the render function)
- Give this URL a symbolic name of "job-detail"

Create the template, `job_board/detail.html`
- Display
	- `posting.title`
	- `posting.company`
	- `posting.description`
	- `posting.salary`

But what if we supply an id that **does not exist**?
- Our application renders an error page
	- Indicates that no item with id 4 exists
- Not very friendly
- See the next video

