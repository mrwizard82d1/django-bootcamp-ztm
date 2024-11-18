Let's implement the create notes "feature"

As a prerequisite, let's create some notes using the admin interface
- Login with "admin" account
- Create note for "Barcelona trip"
- Create second note for "Barcelona trip"

Create or view, `class NoteDetailView(DetailView)`
- `model = Note`

Edit URL (`trip/urls.py`)

```python
path('dashboard/note/<int:pk>', 
	 NoteDetailView.as_view(), 
	 name='note-detail')`
```

Create `trip/note_detail.html`
- Copy from https://github.com/mrwizard82d1/ZTM-Django-auth/blob/master/trip/templates/trip/note_detail.html
- Comment out
	- Anchor tag for note update
	- Form tag for note delete

Allow us to visit note details from within a trip
- Change `trip/trip_detail.html`
- Specify details of anchor tag surrounding the "note details block"

In the next video we will change the app to
- View all of our notes
- Create a note

