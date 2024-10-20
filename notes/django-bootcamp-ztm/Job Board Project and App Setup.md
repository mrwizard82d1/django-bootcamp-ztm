
Setup a project and app

Create a typical default project
- Change name of "project" to `config`
- Put underneath directory `job-board`

Create a file `urls.py` in application
- Copy `config/urls.py` to `job_board` app (`job_boards/url.py`)
- Change `path()` call to `path('', index)`
- Change `config/urls.py` to include 
	-  `path('', include('job_board.urls')` 

Add `index()` to `job_boards/view.py`

Import newly created function into `job_boards/urls.py`
- `from .views import index`

