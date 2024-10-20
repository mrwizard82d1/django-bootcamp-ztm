
Django models give us a way to store data
- Adds "full stack app power"
- "Ingredients" for pizza

So far, all projects
- Matches URL to identify view function
- The view function returns a template containing all your favorite movies

Models:
- Are Python classes
- That interact with a database
- In a single table
- Each variable on the Python class is a **column** on the table

Typical model code:
```python
from django.db import models

class Movie(models.Model):
	title = models.CharField(max_length=100)
```
- Creates a "Movie" table
	- Contains an automatically generated `id` column
		- Starts with 1 and auto-increments
		- 