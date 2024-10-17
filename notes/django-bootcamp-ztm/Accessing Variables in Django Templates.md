Will pass information into template and access it

For example, in `views.py::index()`:
- Suppose we change the context to:
	- `{'movie': 'gladiator'}`
	- This change allows us to use the item of the key `movie` to replace the text `movie` in our HTML

**Note**: the value in the template need not be a singular value but can be a list with the use of additional Django templating language
- An example in the next video

