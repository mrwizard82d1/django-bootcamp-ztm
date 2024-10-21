
Time to create and store data in database
- C(reate)
- R(ead)
- U(pdate)
- D(elete)

Django allows us to **avoid** writing SQL code
- By inheriting from `models.Model`
	- This class implements a "model manager"
	- The "model manager" is implemented by the `objects` attribute of the model; that is, `JobPosting.objects` is the model manager for the JobPosting object/table
- Supports many CRUD operations
	- `JobPosting.objects.all()`
	- `JobPosting.objects.get(id=1)`
	- `JobPosting.objects.filter(title='job title')
	- `JobPosting.objects.filter(company='abc tech')

Django also supports interacting with the database from a terminal
- Activate terminal
- Execute `python manage.py shell`
	- In PyCharm, this opens the shell in a **new window**: Python Console
- First step, `from job_board.models import JobPosting`
- Now we can query and update data
	- `JobPosting.objects.all()` returns empty `QuerySet`
	- `JobPosting.objects.create(title='a job title', ...)`
	- Afterward, `JobPosting.objects.all()` 
		- Returns a `QuerySet` with a single object with `jobposting_id` == 1
	- `job = JobPosting.objects.get(id=1)` 
		- Returns the job posting with `jobposting_id == 1`
	- `job.description = 'a good first job'` 
		- **Changes** the `description` field on job with id 1
	- `job.save()` saves these changes to the database
		- **Remember**, until one enters `job.save()` any changes are **temporary**
		- Once one executes `job.save()` changes are **permanent**
	- `job.delete()` deletes the database object backing the local variable `job`
		- After call to `job.delete()` querying all objects (`JobPosting.objects.all()`) will again return **an empty `QuerySet`**
