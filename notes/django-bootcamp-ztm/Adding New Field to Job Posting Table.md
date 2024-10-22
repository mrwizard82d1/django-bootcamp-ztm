
Add a new field to record if posting is a "draft"
- Add a new member to `JobPosting`
	- `is_active = models.BooleanField(default=False)`

After adding the value to the model, we must migrate the model
- `python manage.py makemigrations`
- `python manage.py migrate`

Add three additional `JobPosting` instances
- These additional instances allow us to set the newly added `is_action` value

