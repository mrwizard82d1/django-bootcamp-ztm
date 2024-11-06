Create the update view
- Include the `UpdateView` class in `views.py`

Add `LinkUpdateView` class
- Inherit from `UpdateView`
- Using functions
	- Create a form
	- Check if request is get or put
	- Either render the form or update and save in our database

Additionally, `LinkUpdateView` edits the same data as `LinkCreateView`
- Therefore, we need **not** specify an additional view
- But can reuse `link_form.html`
