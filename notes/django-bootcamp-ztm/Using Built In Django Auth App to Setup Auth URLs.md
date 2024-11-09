Move in authentication/authorization controlling what users can do
- Leveraging built-in authentication app

Open `settings.py`
- `INSTALLED_APPs` contains `django.contrib.auth`
- This app not inherently different from any other app
- But are pre-configured with Django
- This app deals with authentication / authorization
- Not magical
	- Just like any of the apps we have previously made

Add app to `urlpatterns`
- Open `triptrak/urls.py`
- Add a path for authentication
	- `path('accounts/', include(django.contrib.auth.urls))` 

Including `django.contrib.auth.urls` provides a number of URLs
- See [this post](https://python.plainenglish.io/inbuild-user-authentication-with-django-38b5983a7543) for this list and for an explanation
- `accounts/login/ [name='login']`
-  `accounts/logout/ [name='logout']`
- `accounts/password_change/ [name='password_change']`
- `accounts/password_change/done/ [name='password_change_done']` 
- `accounts/password_reset/ [name='password_reset']`  
- `accounts/password_reset/done/ [name='password_reset_done']`
- `accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']` 
-  `accounts/reset/done/ [name='password_reset_complete']`
- Django provides URLs and views
	- It provides **no templates**
	- That is, we provide the "look and feel" for our authentication / authorization flows

Let's see what happens when we navigate to these AC/AZ URLs **right now** (no templates)
- `accounts/login/` 
	- Produces `TemplateDoesNotExist` page


