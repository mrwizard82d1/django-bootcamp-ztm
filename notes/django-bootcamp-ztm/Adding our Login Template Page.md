Let's create our "login.html" page expected by Django
- Create file in `config` or `triptrak` '/templates/registration/login.html'

Add `<form ...> </ form>` to login page
- Include `{% csrf_token %}`
- Render form using paragraph tags
	- `{{ form.as_p }}`
- Add a `submit` button
- Add a `hidden` input named `next`
	- If not logged in, forward to "next" page

Add logic to handle an already logged in user
- If a "next" page exists
	- If we have no authenticated user
		- The `user` variable has a value from **Django session authentication**

At the top, we have logic to check for errors:
- Check for `form.errors`
- If so, provide generic error message that limits information to "bad guys"

Must tell Django how to find our login page
- Edit `settings.py`
	- Add `[BASE_DIR / 'templates']`
		- But already added in my `settings.py`
		- Newer version?
	- Must describe where should user navigate after login **if not `next`**
		- If we **do not** take this step, the user will return to the "Please login page" after logging in (a bit confusing)
		- Add `LOGIN_REDIRECT_URL = 'trip-list'`
			- Show the "trip list" page after login

Restart server and test

I encountered an error running the code
- Django could not find my newly created template
- I could "work around" the issue by changing `TEMPLATES.DIRS` to
	- `[BASE_DIR / 'triptrak/templates']`
- Eventually, I "discovered" that I had created my template directory **in the wrong place**
	- I had created it as a subset of the "base" application (`triptrak/triptrak/templates/registration`)
	- It should actually be a sibling of the `trip` and `triptrak` directories
		- `triptrak/templates/registration`
- Be warned!

