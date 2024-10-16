Telling Django to look for templates inside each app
- Set the value in `settings.py`
	- `TEMPLATES -> APP_DIRS: True`
- Setting the `APP_DIR` value to `True`
	- Informs Django to
	- Look in each app for templates

The directory format for templates:
- `<app_name>/templates/<app_name>/<html_filename>`
- Concretely,
	- `movies/templates/app/index.html`

After creating the template (file), we must inform Django of this template
- Change the implementation of the `index()`  view
	- Call the imported `render()` method
		- Pass the `request` as the first argument
		- The path to the template as the second argument
		- The (currently empty) "context" as a third argument
		- 