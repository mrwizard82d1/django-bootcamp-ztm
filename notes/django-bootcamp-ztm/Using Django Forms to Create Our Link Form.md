Currently only accessing a single "input field"

Django Forms is an answer to this problem
- Create new file: `links/forms.py`
- Import Django Forms
	- `from django import forms`
- Define a form class
- Within that class, define all the link data
	- Supplied by the user
		- `name=forms.CharField(max_length=50)` 
		- And so on
	- All fields are required **except** the `slug`

We now update our view to use this newly created Django form
- Create a new form: `form = LinkForm()`
- Add this new form (instance) to the context

Add this newly created Django form to the page
- Replace
	- `<input type="text" name="link" />`
	- with `{{ form }}`
		- The name `form` is the name of the form in the `context`

Re-run application to test
- The form rendered in the video is horizontal (left-to-right)
- However, my form renders **vertically** (top to bottom)
- I do not know why
	- I suspect styling of some sort but...

We will have **different** behavior depending on
- Are we showing existing data?
- Are we capturing new data?
- We handle the `GET` / `POST` distinction in `views.add_link()`

This process is so common that Django created a `ModelForm` to perform these steps "out of the box"
