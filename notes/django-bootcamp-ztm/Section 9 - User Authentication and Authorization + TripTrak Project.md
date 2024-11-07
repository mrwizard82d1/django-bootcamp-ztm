Building a project and letting users log in

Create project
- Using VSCode
	- Create a project directory named `video`
	- `python -m venv env`
	- `source env/Scripts/activate`
	- `pip install django`
	- `django-admin startproject config .`
		- Created in `video` directory
	- `python manage.py startapp trip`

Create project using PyCharm
- Select "New Project" in PyCharm opening screen
- Select "Django" project
	- Name: "triptrak"
	- Interpreter type: "Custom environment"
	- Environment: "Generate new"
	- Type: `Poetry`
	- More settings
		- Application name: "trip"
		- Accept remaining defaults
	- Press "Create" button
- Add `.gitignore` 
	- For Python
	- For JetBrains IDE

Initial project view
- Edit `settings.py`
	- Add `trip` to `INSTALLED_APPS`
- Create and edit `trip/urls.py` by copying `triptrak/urls.py`
	- Remove include of `admin`
	- Add to `urlpatterns`
		- `path('', ), // temporarily blank`
- Edit `config/urls.py` (or `triptrak/urls.py`)
	- Add `django.urls.include`  function
	- Add to `urlpatterns`
		- `path('', include('trip.urls')`
- Edit `trip/views.py`
	- Create a base view
		- A class-based view to render a template
		- `include django.views.generic import Template View`

```python
class HomeView(TemplateView):
	template_name = 'trip/index.html'
```

- Edit `trip/urls.py`
	- Add `from .views import HomeView`
	- Change to `path('', HomeView.as_view(), name='home')`

Create project
- Create `index.html` template
	- Create directory `trip/templates/trip`
	- Create file `index.html` in the `trip/templates/trip` directory
		- `<h1>Trip Tracker</hl>`

Run application
- In VSCode
	- `python manage.py startapp trip`
	- `python manage.py runserver`
	- The video encountered an error: `trips` instead of `trip`
		- Correct: `trips` -> `trip` in `settings.py`
- In PyCharm
	- Click the run button for "triptrak"

Success!
