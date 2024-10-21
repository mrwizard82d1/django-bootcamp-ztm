
Creating our first model(s)

Remember, creating an app
- Creates a `models.py` file for that app

A Django model
- Is a Python **class**
- Represents a table in the database
	- Although we are currently targeting `db.sqlite3` model
	- It is easy to move
- The model attributes are the **fields** in a database **table**

Concretely, we are creating a model of a job posting
- Job posting table
	- With fields
		- title, description, company, salary

Consequently, we create a Python class that
- Inherits from `models.Model`
- Has attributes
	- `title`
	- `description`
	- `company`
	- `salary`

Since we are **changing** our data model, we must
- Make migrations (using the `makemigrations` `manage.py` sub-command
	- Create the "instructions" telling Django how the database will change
	- For example, suppose that, after we have created the table, we choose to add a new field. Running `makemigrations` would create the instruction to add this new field
- Migrate the table (using the `migrate` `manage.py` sub-command)
	- This step is the action of applying the latest migrations; that is, this step actually changes the database
	- Similarly, after creating  the migrations to add a new field, running `migrate` will actually add that field to our table