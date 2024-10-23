Django admin authentication and authorization **built-in** to Django
- A great feature
	- Time savings
	- And reliability 
		- Tough to implement my own 
			- Authorization 
			- Authentication

We currently see the default features of the admin interface
- But nothing specific to our application
- We must register our application
	- Open `job_board/admin.py`
	- Add `admin.site.register(JobPosting)`
		- Be sure to import
			- `from .models import JobPosting`
- Navigate to 'admin/'
	- We now see our "Job Board" section
	- And "Job postings"
	- Click on the link, "Job postings"
		- We see the three job postings that we previously created using `manage.py`

The problem with the default interface
- Everything wires up correctly
- We can navigate to see all our job postings and the details of a specific posting
- However, each posting has a "generic" name
	- For example, `JobPosting object (1)`
- We will change this behavior in the next video


