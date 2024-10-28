Our view uses an **empty** `context`
- We want to fill it based a database query

Change `links/views.py`
- Import `Link` from `.model`
- Query all available objects
	- `Link.objects.all()`
- Incorporate all these returned links into the `context`
	- `context = {'links': links}`

Incorporate the context - the links - into the template
```html
<ul>
	{% for link in links %}
		<li>{{ link.name }}
	{% endfor %}
</ul>
```

Next up, we will style our page using tailwind
