Now that we've created our tables and migrations...

Register models with admin
- Import `Profile, Link`
- `admin.site.register(Profile)`
- `admin.site.register(Link)`

Create application admin superuser
- Name: `lajones13f9`
- Email: `lajones13f9@gmail.com`
- Password: Password Safe

Create some profiles and links
- Profile
	- Name: "Larry Jones"
	- Slug: "mrwizard82d1"
	- Background color: "Blue"
- Links
	- First
		- Text "My Website"
		- URL: https://www.martin.com
		- Profile: "Larry Jones"
	- Second
		- Text: "Twitter Profile"
		- URL: https://twitter.com/mrwizard82d1
		- Profile: "Larry Jones"

Repair appearance of links ("Link object 1")
- Change `models.py`
- Define `__str__()`
	- Return `f'{self.text} | {self.url}'`

