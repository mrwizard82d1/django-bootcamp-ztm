Create the ability to add a link to our profile
- Use generic `CreateView`

Create class `LinkCreateView`
- Inherits from `CreateView`
- Replaces code to
	- Create `forms.py` file and forms
	- Check if this was a post or a get request
	- Return an empty form or save the form data
- Include
	- `model = Link` (expected)
	- `fields = '__all__'` - include all `Link` fields
	- `success_url = reverse_lazy('link-list')`
		- This link causes navigation to `link-list` when successful

Add view to URL
- Edit `link_plat\urls.py`
- Add new path to `urlpatterns`

Create a new form
- Filename: `templates\link_plant\link_form.html`
- Extend file 'link_plant/\_base.html'
- Include `block content` section
	- Add styled "Link Form" header
	- Separated by a horizontal rule
	- Create a form to submit using `POST`
		- Include the `{% csrf_token %}`
		- Include the passed in form (`{{ form }}`)
	- Add a "Save Link" submit button
