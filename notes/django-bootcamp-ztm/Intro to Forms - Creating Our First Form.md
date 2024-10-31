Dive into Django forms

We'll create a view URL and template for our form feature
- Open `links/views.py`
- Add `add_link()`
	- This function simply calls
		- `render(request, 'links/create.html', {})`
- Add another route
	- `path('link/creat/', add_link, name='create-link')`
- Create the template
	- New file `templates/links/create.html`
	- Extend `links/_base.html`
	- Followed by block
		- Within the `block content`
		- Add a form
			- Two `input` fields
				- `<input type="text" />`
				- `<input type="submit" value="Create />"`

Let's test our code so far
- Start application
- Navigate to `localhost:8000/link/create
- Hover to the left of the text create
	- We see an text input box
	- Enter some text (doesn't matter)
	- Press `Create` "button"

But nothing appears to happen!?
- See the page re-render; however, the link is now
	- 'localhost:8000=/link/create?'
- By default, pressing the submit button, labeled 'Create', invokes an HTTP **Get** method
	- Used to **get** data
- However, `/links/create` should
	- Send a **Post** request to the Django server to create a new link
- As confirmation, our terminal reports a 'GET' request for `/links/create`

We will look into how to get the data from the form in the next video