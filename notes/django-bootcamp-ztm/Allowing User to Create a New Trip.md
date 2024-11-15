We generally want to allow a user to create a new trip from the dashboard

We have some predecessor tasks:
- Install `crispy-tailwind`
	- In shell, `poetry add crispy-tailwind`
	- Add `crispy-tailwind` to IDE project interpreter
- Modify `settings.py`
	- Add to `INTALLED_APPS`
		- `'crispy_forms'`
		- `'crispy_tailwind'`
	- Add environment variables
		- `CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"`
		- `CRISPY_TEMPLATE_PACK = "tailwind"`

Set up our trip create view

```python
class TripCreateView(CreateView):
	model = Trip
	success_url = reverse_lazy('trip-list')
	fields = ['city', 'country', 'start_date', 'end_data']

	# Create a template named like "model_form.html"

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)
```

Create the template, `trip_form.html`
- Remember that the **model** is 'trip'
- Extends `trip/_base.html`
- `{% load tailwind_filters %}`
- Include form inside `block content`  pair

```python
{% block content %}
	<h1>Trip Form</h1>
	<form action="" method="POST">
		{% csrf_token %}
		{{ form|crispy }}
		<input type="submit"... />
	</form>
{% endblock content %}
```

Add the URLs to `trip/urls.py`:
- `path('dashboard/trip/create/', TripCreateView.as_view(), name='trip-create')`

Add links to `trip/_base.html`
- "My Trips" becomes
- `<a href="{% url 'trip-list' %}">My Trips</a>`
- `<a href="{% url 'trip-create' %}">New Trip +</a>`