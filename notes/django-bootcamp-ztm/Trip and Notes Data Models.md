Let's set up our models

Open `trip/models.py`
- Want to create two models / tables
	- Trips
	- Notes (associated with a trip)
		- Also include **images**

Model a trip
- `class Trip(models.Model)`
	- `city`
	- `country` as a **code**
	- `start_date`
	- `end_date`
		- Both start and end data can be either 
			- Blank
			- Null
		- That is, neither `start_date` nor `end_date` is required
	- `owner`
		- A reference (foreign key) to an authenticated user
		- Delete this authenticated user => delete all their trips
		- Provide a "link back", `trips`, 
			- Using the `related_name` parameter
			- That is, one can query **trips** from the **user**
	- Implement `__str__()`

Model a note
- `class Note(models.Model)`
	- `trip`
		- Refers back to a specific instance of a `Trip`
		- Delete a `Trip` => delete all its `Note`s
		- Provide a "link back" named "notes" on each `Trip`
	- `name` - a human readable identifier for this note
	- `description` - Details of this note
	- `type` - Used to categorize events
		- Define constant (using a `tuple)
			- `EXCURSIONS`
	- `img` - An image for this `Note`
		- Using a parent directory of 'notes' in the `upload_to` parameter
			- This action will cause the 'notes' directory **to be created** by Django at runtime
	- `rating` - Rating whatever this `Note` is about
		- A model of type `PositiveSmallInteger`