
How do we present a **list** of our favorite movies
- Define our context with a **list** of movies
- Change `index()` to render a list

Typically `context` variable 
- Defined
- Passed into `render(..., ..., context)` call 

Changes to `index.html`
- Add logic with variables, tags, and filters
```python
{% if movies %}
	<ul>
		{% for movie in movies}
			<li>{{ movie:title }}</li>
		{% endfor %}
	</ul>
{% else %}
	<p>No favorite movies...</p>
{% endif %}
```
