
Time to share our project with the world

The following items are the predecessor tasks to run our project on a server.
- Open project
	- Activate virtual environment
- Update `settings.py`
	- Change `ALLOWED_HOSTS` to allow any ('\*') host
- Install `gunicorn` into the application virtual environment
	- 'Green unicorn'
	- "A Python WSGI HTTP Server for UNIX"
	- [gunicorn web site](https://gunicorn.org)
- Create a `requirements.txt`
	- Execute the command `pip freeze >requirements.txt` in a terminal
