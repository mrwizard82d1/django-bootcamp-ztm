Finish our models by handling images

Change environment
- Install `pillow`
	- Already done in PyCharm

Must provide additional configuration in `settings.py`
- Add two configured constants to bottom
	- `MEDIA = /media/` - site URL for images
		- For example, this configuration allows our application to recognize resources at `www.my-site.com/media/img-1`
	- `MEDIA_ROOT = BASE_DIR / 'media/` - OS path for images
		- This line takes advantage of features in `pathlib`

Must tell Django how to serve images by editing `triptrak/urls.py`
- Add to imports
	- `from django.conf import settings`
	- `from django.conf.urs.static import static`
- Must add to `urlpatterns`  if running in debug
	- `static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)`

Register models with our admin (edit `trip/admin.py`)
- Import `Trip` and `Note`
- Register models
	- `admin.site`

Since we've changed our **model**, we must **migrate** our stored data
- `python manage.py makemigrations`
- `python manage.py migrate`
- 