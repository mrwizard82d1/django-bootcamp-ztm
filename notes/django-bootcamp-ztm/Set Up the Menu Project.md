Want to display our menu
- On the website
- On a mobile app
- On in-store display screens

Approach
- Create a typical Django app
- Change it to serve data 

Create the Django project using VS Code
- Execute
```bash
cd video # root
python3 -m venv env
source env/Scripts/activate
pip install django
django-admin startproject config .
python manage.py startappp menu
```

- Add `menu` to 'INSTALLED_APPS' section of `settings.py`

Create Django project using PyCharm
- Directory `django-bootcamp-ztm/code/menu_app`
- Python version; 3.12
- App name: `menu`
- Project name: `config`

Add application to `settings.py`
- Add `menu` to 'INSTALLED_APPS'

Test application (Django test page)
