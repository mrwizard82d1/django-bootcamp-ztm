Let's update and delete our notes

Create our view(s)
- Copy `NoteCreateView`
	- Change class declaration to `NoteUpdateView(UpdateView)`
	- Change references to `NoteCreateView` to `NoteUpdateView`
- Create `NoteDeleteView(DeleteView)`
	- `model = Note`
	- `success_url = reverse_lazy('note-list)`
	- **BEWARE** 
		- This view **does not** need any additional code, but we must send a `POST` request to delete the note.

Change `trip/urls.py`
- Append two additional URLs

```python
path('dashboard/note/<int:pk>/update/', 
	 NoteUpdateView.as_view(), name='note-update')
path('dashboard/note/<int:pk>/delete/', 
	 NoteDeleteView.as_view(), name='note-delete') 
```

We need create no views
- `delete` does not need a template
- `update` **reuses** the create `note_form.url`
- Update `note_detail.html`
	- Add anchor tag that invokes `note-update`
	- Add a form with a `POST` method for delete

Next we'll update and delete an entire trip
