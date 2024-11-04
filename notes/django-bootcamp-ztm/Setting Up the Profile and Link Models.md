Create model and tables for application
- Go application directory (`link_plant`)
- Edit `models.py`

Create a `Profile` class (a model)
- Attributes
	- `name` (`models.CharField`)
	- `slug` (`models.SlugField`)
	- `bg_color` (`models.CharField`)
		- Specify both
			- `max_length`
			- `choices` (initialized from a class constant)
				- <`column name`> -> <`human-readable column name`>
- Implement `__str__` method

Create a `Link` class (another model)
- Attributes
	- `text` (`models.CharField)
	- `url` (`models.URLField)`)
	- `profile` (`models.ForeignKey`)
		- The `Profile` instance with which this `Link` is associated
		- `on_delete=models.CASCADE`
				- When `Profile` is deleted
		- `related_name='links'`
				- The `related_name` parameter results in an additional parameter, `Profile.links` to be added to the `Profile` class. 
				- The value of `Profile.links` allows navigation from a single `Profile` to **all** of its `Link`s
		- One `Profile` may relate to **many**  links

Migrate database
- `python manage.py makemigrations`
- `python manage.py migrate`
