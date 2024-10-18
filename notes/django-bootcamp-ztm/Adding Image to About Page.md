
We want to add an image to our "about" page
- Adds "pizzazz"

Note that `config/settings.py` specifies a setting named
- `STATIC_URL`
- The value of this variable is `static/`
	- This is the **directory** from which are application will serve 
		- **Static** content
			- Fixed HTML pages
			- Images
			- And so on

By default, Django will look for the `static/` folder **inside of an app**
- Therefore,
	- Create a new directory in the `movies` app
	- Called `static`
	- And containing a sub-directory name `movies`
		- That is, the `movies` directory must contain a tree:
			- `static`
				- `movies`

Copy image to `moves/static/movies`

Change `about.html`
- Add template to load static resources
- Display the image we copied (`mrwizard_2.jpeg`)
- To refer to the image in the template
	- One must use the path relative to the `static` directory
		- For example, `movies/mrwizard_2.jpeg`

