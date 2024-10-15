Create project
- Either using command line (from video)
- Or using `PyCharm`

Create a temporary view
- Use function named `index`
- `index()` simply returns an `HttpResponse` with an "informative" message

Add appropriate URL
- Add `urlpattern`
	- `path("", index)`
			- A "default" view for an empty "path"
