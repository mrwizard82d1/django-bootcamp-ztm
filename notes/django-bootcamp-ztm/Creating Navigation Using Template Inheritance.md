
An example of using template inheritance in "real life"

For example, add navigation to home page:
```html
<block>
	<div>
		<a href="">Fav Movies</a>
		<a href="/about">About</a>
	</div>
# ...
</block
```

This change correctly renders the navigation links on the **home** page but **fails** to render the navigation links on the `about/` page
- Since we just have two pages, we could simply copy-paste
- However, the copy-paste solution is **not** effectively scalable
	- Violates the DRY principle

Another issue
- Currently hard-coding `href` tags
- For a small number of pages, one could simply change **all** the references
- However, Django provides a better alternative
 
 The `path()` function in the `urlpatterns` array in `urls.py` takes an optional third argument, `name: str`
- This argument allows use to specify a particular HTML page symbolically
- For example, add 
	- `name=home` to `path()` call for the "home" page
	- And `name=about` to `path()` call for the about page
- And change the hard-coded URL in the call to href with:
```HTML
<a href={% url 'home' %}>Fav Movies</a>
<a href={% url 'about' %}>About</a>
```

Extract the "navigation" `<div>` in `index.html` into a separate file

Change the files
- `index.html`
- And `about.html`
- To be extended by  `_base.html`
	- But **override** the `content` block defined in `_base.html`



