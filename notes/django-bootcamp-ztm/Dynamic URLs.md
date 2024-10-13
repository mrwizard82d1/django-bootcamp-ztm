Algorithm to match request URL to view function described in the first section of the [Django tutorial](https://docs.djangoproject.com/en/5.1/intro/tutorial01/)

General steps:
- Run-time determines the root URL configuration
	- Typically using environment variable `ROOT_URLCONF`
		- This value typically refers to the module, `urls.py`
	- But could be `urlconf` attribute of `HttpRequest` (only if **set**)
- Loads the module specified in the previous step
- Looks for the `urlpattern` variable in the Python module
- Searches through each pattern (from top to bottom) looking for a match to the requested URL
	- Search stops at **first match**
- Imports the function specified in the `path`
- Invokes the specified (view) function
	- The requested URL specified as part of `HttpRequest`
	- If the matched URL **pattern** contains **named groups**
		- The values captured in this named groups are passed as positional arguments to the function
	- Keyword arguments allow passing additional arguments
		- Which may be **overridden** by `kwargs` passed to:
			- `django.urls.path()` or
			- `django.urls.re_path()`
- If no such match is found or an error occurs,
	- Django invokes an error handling page