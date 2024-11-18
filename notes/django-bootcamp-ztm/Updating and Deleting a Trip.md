Let's perform similar work for a Trip that we just completed for a Note

Edit `views.py`
- Create `TripUpdateView(UpdateView)`
	- Minor, appropriate modifications from `NoteUpdateView`
	- Remember, we do not want the **owner** field to be selected so we specify the fields of interest
```python
fields = ['city', 'country', 'start_date', 'end_date']
```

- Remember that our template will be named
	- `<model>_form`
	- That is, `trip_form`
	- Which we already have

- Create `TripDeleteView(DeleteView)`
	- Again, simple replacement of text 'Note' with 'Trip'

We are finally up to aesthetics for the the remainder of our pages

