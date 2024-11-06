Add a delete view

Add `LinkDeleteView` to `views.py`
- Import `DeleteView` from `django.views.generic`
- Add class `LinkDeleteView(DeleteView)`
	- If using a function-based view
		- Take in an id (primary key) on an object (to delete)
		- Query the database for that object
		- If the object exists, delete it
		- Either return some template or forward the user to some URL
	- `DeleteView` simplifies the process
		- `model = Link`
		- `success_url = reverse_lazy('link')`
		- Default behavior
			- View supplies an "Are you sure?" type page
			- Expects a template generically named
				- `<model>_confirm_delete.html`
				- In other words, `link_confirm_deletel.html`

Change `urls.py`
- Add path `link/<int:pk>/delete`
- View is `LinkDeleteView`
- Name is `link-delete`
- Remember that `LinkDeleteView` **confirms** the deletion request

Create view
- New file `templates/link_plant/link_confirm_delete.html`
- In content
	- Ask the user, "Are you sure you want to delete this?"
	- Add a form "Submit" executing the `POST`

Edit `link_list.html` to include delete button


