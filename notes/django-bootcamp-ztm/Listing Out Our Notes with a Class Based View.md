We want to list out all of our notes **without** going through a trip

Create our view
- Edit `trip/views.py`
- Create class `NoteListView(ListView)`
	- `model = Note`
- Override the `get_queryset(self)` method
	- Filter all notes to only those notes written by the currently logged-in user
		- Use keyword `trip__owner`
			- Note the double underscore separator (`__`)
			- This construction causes the Django runtime to
				- Navigate the `trip` foreign key in the `Note`
				- Collect the `owner` field from the `Trip` object

Add the URL:

```python
path('dashboard/note', NoteListView.as_view(), 
	 name='note-list')
```

Create our template
- Based on our rule to name templates; that is, `<model>_list.html`, we create `templates/trip/note_list.html`
	- Copy template from [GitHub](https://github.com/mrwizard82d1/ZTM-Django-auth/blob/master/trip/templates/trip/note_list.html)
	- (Temporarily) Remove anchor surrounding "New Note +"

Change `templates/trip/_base.html`
- Surround "My Notes" with link
- `<a href="{%  url 'note-list' %}">My Notes</a></li>`

Run and test!
