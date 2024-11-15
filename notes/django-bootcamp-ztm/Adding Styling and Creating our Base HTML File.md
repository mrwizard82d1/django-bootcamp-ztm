Time to make the app appear "spiffier" and to reorganize code a bit

Add `trip/templates/trip/_base.html`
- Copy contents - including formatting - from [repository](https://github.com/mrwizard82d1/ZTM-Django-auth/blob/master/trip/templates/trip/_base.html)
- Remove "future code" 
	- That is, anchor tags

Update `trip/templates/trip/trip_list.html`
- Inherit from `_base.html`
- Also remove "future code"
	- That is, the wrapping anchor tag

We now have:
- A "navbar" on the left-hand side of the trip list page
- We can logout from the trip list page
	- And it now works correctly (in my code)

Logout and redirect issue
- The code that I have used as a "go-by" in Dominic's GitHub repo is **final** code
	- In other words, the code at the **end** of this lesson
- When copying this code from the GitHub repo, one must
	- **Remove** code from future lessons
- Additionally and most importantly,
	- At some time in the past, I created an environment variable, `LOGOUT_REDIRECT_URL = 'trip-list'`
	- I think I created this environment variable because of the code in the [Django 5 login, logout, and sign-up article](https://learndjango.com/tutorials/django-login-and-logout-tutorial) that I have mentioned previously. This article sets **both** values in `settings.py`
		- `LOGIN_REDIRECT_URL`
		- `LOGOUT_REDIRECT_URL`
	- When I remove `LOGOUT_REDIRECT_URL` (similar to what happens in the [repository](https://github.com/mrwizard82d1/ZTM-Django-auth/blob/master/trip/templates/trip/_base.html)), then I see the behavior demonstrated in the video.
