We can now see notes but can only create them using the admin screens. Let's fix that.

Create a view:
- In `trip/views.py`
- Create `class NoteDetailView(DetailView)`
	- `model = Note`
	- `success_url = reverse_lazy('note-list')`
	- `fields = '__all__'`
- However, the form the user must fill out must have access to the trips of **only the current user**

```python
form = super(NoteCreateView, self).get_form(**kwargs)
trip = Trip.objects.filter(owner=self.request.user)
form.fields['trip'].queryset = trips
return form
```

Add a URL to `trips/urls.py`

```python
path('dashboard/note/create', NoteCreateView.as_view(), 
	 name='note-create')
```

- **NOTE** this path entry must be **before** the `path` for 'dashboard/note'; otherwise, "first one wins" and Django will **never** look for 'dashboard/note/create'

Create the expected template
- The expected form of the template file name is `model_form.html`
- Create the file `templates/trip/note_form.html`
- We have a specific need for our `form`
	- `enctype=multipart/form-data`
		- This type encoding is needed because our information includes **both**
			- Typical textual response
			- An optional image

Change `template/trip/_base.html`
- Surround the text "New Note +" with an anchor tag

```html
<a href="{%  url 'note-create' %}">New Note +</a></li>
```

We can now create a new note
