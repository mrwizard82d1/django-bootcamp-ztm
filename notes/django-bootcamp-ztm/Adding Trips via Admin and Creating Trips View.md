Create superuser

Run server

Add a couple of trips:
- Trip 1
	- City: "Barcelona"
	- Country: "SP"
	- Start and end data: some dates a couple of years in the past
	- Owner: myself
- Trip 2
	- City: "Chicago"
	- Country: "US"
	- Start and end data: some dates in the past
	- Owner: myself

Create a view so we can see all our trips
- Edit `trip/views.py`
	- `from .models import Trip, Note`
	- Create function to present all `Trips` 
		- Named `TripsList`
		- Query all `Trip` objects
		- Add all `Trip` objects to context
		- **Return** `render(request, 'trips/trips_list.html', context)`

Add URL to `trip/urls.py`
- Add new pattern to `urlpatterns`
	- `path('dashboard/', TripsList, name='trip-list')`

Create the template, `trip/trips_list.html`
- Include a header, `<h1>My Trips</h1>`
- Loop over all trips
	- Present an unordered list of
		- `trip.city()) | trip.country()`
