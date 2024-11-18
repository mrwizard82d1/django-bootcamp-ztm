Currently, clicking on a trip is a "no op". Let's fix this.

Create a new view
- Go into our `trip` app
- Create class `TripDetailView`
	- Inherit form `DetailView`
	- Our `model` is the `Trip`
	- **But** we also want data from all the `Notes` associated with this trip
		- Override `get_context_data()` to address this issue
		- Get the **original** context
			- `super().get_context_data(**kwargs)`
		- Add the `Notes` associated with this `Trip`
]
```python
trip = context['object']
# Collect **all** `Notes` associated with this Trip
notes = trip.notes.all()
context['notes'] = notes
return context  ## with trip notes
```

Let's wire up our URL to use the new view
```python
path('dashboard/trip/<int:pk>/',
	 TripDetailsView.as_view(),
	 'trip-detail')
```
 
Create a template
- File `templates/trip/trip-detail.html`
- Copy from `https://github.com/mrwizard82d1/ZTM-Django-auth/blob/master/trip/templates/trip/trip_detail.html`
- **Remove** section of code to **delete** a trip
- **Remove** anchor tag (but not the `div`) to **create a note**

Update `trip/trip_list.html` to add a link to view the details
- At top-level `div` insert an anchor tag
	- `href="{% url trip-details trip.pk %}"`
- Reformat

Test the view
- Remember that we have **created no notes**

We will create notes to be display in the next video
