Begin by running the (default) migrations
- `python manage.py makemigrations`
	- The video discovered an error
		- Change `import django.utils` to `django.utils.txt` (But I had already done this)
- `python manage.py migrate`

Register model (`Link`) with the "built-in" `Admin` app
- Open `admin.py`
- Add reference to `models.Link`
- Register site
	- `admin.site.register(Link)`

Create superuser
- `python manage.py createsuperuser`
	- Supply details

Run application and log in as super user

