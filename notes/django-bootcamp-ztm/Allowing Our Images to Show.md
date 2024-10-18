
We will change our application to display static files

Steps
- Install `whitenoise`
	- "Radically simplified static file serving for WSGI applications"
- Change `settings.py`
	- Add `whitenoise` middleware after SecurityMiddleware
	- Add
		- `STATIC_ROOT=staticfiles`
		- `STATICFILES_STORAGE=whitenoise.storage.CompressedManifestStaticFileStorage`
- Create `build.sh`
```bash
#!/usr/bin/env bash

# exit on error
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```
- Commit all changes and push to GitHub

Must change Render configuration to use newly committed `build.sh`
- Navigate to project
- Select "Settings"
- Select "Build Command"
	- Change to invoke newly created shell script, `./build.sh`
- Let Render build and re-deploy application
	- Remember that it **takes some time** since its free

