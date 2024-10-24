Create the `links` app
- `python manage.py startapp links`

Add new app to installed apps in `settings.py`
- `links`

Create models to store app data in database
- `name` `CharField` 50 characters, unique is true
- `url` `URLField` 200 characters
	- Full URL that we are replacing
- `slug` `SlugField` unique is true, blank is true
	- `blank=True` allows one to enter no value; however, our application will then calculation a non-blank, unique value for our slug
- `number_of_clicks` `PositiveIntegerField` with default value of zero (0)

Define the `__str__` method of our model

Define additional methods for common actions
- For example, increment the number of clicks
	- `click(self)`
- **Override** the `save(self)` method
	- If no `slug` supplied
		- Generate a `slug` using `django.utils.text.slugify`

