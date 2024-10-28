One must setup:
- A view
- A URL
	- Include this URL in our main project URL

Add `urls.py` to `link` app
- Copy `link_shortener/urls.py` and change
	- Use `index` for view

Change `link_shortener/urls.py`
- Add new path with
	- Empty route
	- `include('links.urls')`

Create `index(request)` in `views.py`
- template_name is `links.index.html`
- `context` is empty dictionary (`{}`)

Create new template `index.html`
- Add template directory to `links` app
	- `templates/links/index.html`
- Template simply renders an `h1` header with some text
	- Just so we can visualize it quickly

Start app
- Note that `index` **was not** imported into `links/urls.py` in the video which caused an error when starting
 
After correcting, app starts successfully
- Not quite.
- I did not originally **return** the result of the `render()` function in `views.index()`. This action resulted in a run-time error.

