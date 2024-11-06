Everything work but needs to be "prettier"

Create `_base.html`
- Copy and paste [code from GitHub](https://github.com/vacchiano/ZTM-Django-cbv/blob/master/link_plant/templates/link_plant/_base.html) into `_base.html`
	- Import `tailwindcss`
	- Create header for navigation (with "LinkPlant" logo)
	- Create a nav item for `link-list`
	- Create `div` container for child content

Change `link_list.html`
- Create a table
- Table body loops through all links
	- Each item has
		- Text
		- URL
		- Profile
		- Button to edit (later)
	- Note that I needed to comment out the
		- URL
		- Profile
		- Button to add