Let's look at Django "behind the scenes"
- The code for Django "pre-installed" apps

Look in `lib/site-packages` of virtual environment
- Open `django.contrib.auth` package
- See a pre-written Django application
- Can discover that `LoginView` looks for the template
	- `registration/login.html`
