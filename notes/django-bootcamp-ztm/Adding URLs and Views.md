Django structure
- Single "project"
	- For example, `config`
- Multiple apps
	- Separation of concerns
	- For example, `my_app`

Created by
- `python manage.py startapp my_app`
	- `my_app` is a project name

Informing runtime of new project
- Edit `settings.py`
	- Add new app, for example, `my_app`

Add views
- Edit `views.py`
	- Initially, use function views
		- Eventually, use class-based views
	- Write function `index()` in `views.py`

However, Django does not (yet) know when to call our newly created function
- Edit `config/urls.py`
	- Add mapping from home page (`''`) to `index` function
