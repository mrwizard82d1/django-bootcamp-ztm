Will demonstrate **class-based views**

Create new project
- VS Code
	- Create new directory
	- Create new virtual environment (`.venv`) in project directory
	- Activate virtual environment
	- Create skeleton project
		- `django-admin startproject config .`
	- Create application
		- `python manage.py startapp link_plant`
- PyCharm
	- File > New Project
		- Select Django project
		- Name: `link_in_bio`
		- Select `Poetry`
		- Application: `link_plant`
		- Press "Ok"

Change `settings.py`
- Add local app, `link_plant`

Run server to verify operation
