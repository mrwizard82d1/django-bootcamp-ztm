We start by creating some trips for our newly created user
- Navigate to `/admin`
	- Must login using administrator credentials
- Add a trip
	- First trip
		- City: Milan
		- Country: IT
		- Owner: test-user
	- Second trip
		- City: Sydney
		- Country: AU
		- Owner: test-user

Return to `dashboard/`
- Logged in as administrator
- But I see the trips for **all users** 
- Fix by one small change to view for this page

Edit `trip.views.py`
- Result returned by `trips_list()` currently  created from
	- `Trip.objects.all()`
- Instead want to filter all the `Trip` objects to only those trips owned by the currently logged in user
	- `filter(owner=request.user)`
		- `owner` is a field on the database
		- `request.user` is the User making the request on this page

Navigate back to 'dashboard'
- On refresh of page, displayed trips only belong to the admin account
- Logout and log in as 'test-user'
	- Now displayed trips only belong to the 'test-user' account

I appear to have discovered **another** change moving to Django 5.x
- The video simply changes the expression
	- `Trip.object.all()` in the function `trips_list()` in the file 'trip/views.py'
	- To `Trip.object.filter(owner=request.user)`
- This change, unfortunately, breaks the application with the error:

```
TypeError at /dashboard/
Field 'id' expected a number but got <SimpleLazyObject: <django.contrib.auth.models.AnonymousUser object at 0x10717bc50>>.
```

  - To repair this error, I used the information from the "AI Overview" in response to the search request: "django error getting objects after logout"
	  - Specifically, I used this section

```
Handle Anonymous Users:
If you need to access objects that are not user-specific, ensure that your logic handles cases where the user is not authenticated:
Python


     def my_view(request):
         if request.user.is_authenticated:
             # Access user-specific data
         else:
             # Handle anonymous users
```

- This change repairs the error
