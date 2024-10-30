Add functionality to redirect from shortened link to actual

Start with `views.py`
- Create function `root_link`
	- Converts (and navigates to) actual link from shortened link

Get information about the link by:
- Call `get_object_or_404()`
	- Passing 
		- `Link` - the model
		- `slug=link_slug` - The "query" of the value of interest

Increment the link count
- Simply call the method we wrote, `link.click()`

Redirect the use to the resource identified by the long link
- `return(redirect(link.url))`

Configure the URL used by `views.root_link()`
- Add a call to `path('<str:link_slug>/', root_link, name='root-link')`

Update `index.html` to link to the (symbolic) URL
- Change `<p>` containing text "Open /{{ link.slug }}"
- The `href` property should now be 
	- `{% url 'root-link' link.slug %}`
- Add attribute `target="_blank` so opening a link actually
	- Opens that link in a new tab