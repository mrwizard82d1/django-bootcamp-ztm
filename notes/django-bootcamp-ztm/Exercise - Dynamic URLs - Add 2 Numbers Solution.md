
Two steps:
- Create a view function
	- `add(request, num1, num2)`
- Create a new route
	- `path(add/<int:num1>/<int:num2>/, add)`