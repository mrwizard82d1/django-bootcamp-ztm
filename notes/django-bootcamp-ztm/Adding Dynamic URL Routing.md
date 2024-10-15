Django supports matching URLs with "named paramaters" for "variables"
- For example,
	- Write a view function 
		- Taking an additional **parameter** of the first name
			- `localhost:8000/hello/Larry/`
		- For example:
			- `hello(request, first_name)`
	- Add a URL specifying the function name **and** the replaceable, typed parameter
		- For example, `path('hello/<str:first_name>/', hello)`
		- NOTE: with a replaceable parameter
			- The trailing slash ('/') is **required**

