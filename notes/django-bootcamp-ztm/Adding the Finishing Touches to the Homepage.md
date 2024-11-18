Our home page is a little bland

Copy code for `template/trip/index.html` 
- From [the Github page](https://github.com/mrwizard82d1/ZTM-Django-auth/blob/master/trip/templates/trip/index.html)

And, of course, I rediscover the fact that I can **no longer** use a 'GET' method to logout, but must use and submit a **form**
- Again, see [the Django login and logout tutorial](https://learndjango.com/tutorials/django-login-and-logout-tutorial)
- Or see 
	- The post, [[Creating Logout Page and Checking User Login-Logout]]
	- And the code in `template/trip/_base.html`

Let's update the login form next
- Copy code from [the Github login page](https://github.com/mrwizard82d1/ZTM-Django-auth/blob/master/templates/registration/login.html)
- Paste it into `templates/registration/login.html`

Update the signup page next

- Copy code from [the Github signup page](https://github.com/mrwizard82d1/ZTM-Django-auth/blob/master/templates/registration/signup.html)
- Paste it into `templates/registration/signup.html`

And we're (almost finished).
