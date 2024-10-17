
Review Django template language documentation
- Variables
	- Outputs a value from the `context`
	- Replaces value like `{{ first_name }}` and `{{ last_name }}`
	- For example, if templated text is:
		- `My first name is {{ first_name }}. My last name is {{ last_name }}.`
	- And the context is:
		- `{'first_name': 'John', 'last_name': 'Doe'}`
	- Then the template renders to:
		- `My first name is John. My last name is Doe.`

### Variables 

Bracketed text uses a syntax that sometimes differs from Python syntax:
- `{{ my_dict.key }}`
- `{{ my_object.attribute }}`
- `{{ my_list.0 }}`
- In general, the syntax to access members of different Python objects is **identical**
	- But it may differ from the actual Python syntax

### Tags

"Tags provide arbitrary logic in the rendering process"

Surrounded by `{%` and `%}`
- For example, `{% csrf_token %}`

Most tags accept **arguments**
- `{% cycle 'odd' 'even' %}`
- I'm uncertain what this would render... (but see the [documentation for built-in tags and filters](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/) below.)

Some tags **require** beginning and ending tags
- `{% if user.is_authenticated %}Hello, {{ user.username }}.{% endif %}`

See [this link](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/) for the documentation of built-in
- Tags
- Filters

And see [this other link](https://docs.djangoproject.com/en/5.1/howto/custom-template-tags/) for information on creating **custom** tags and filters

### Filters

"Filters transform the values of variables and tag arguments"

For example,
- If the filter is `{{ django|title }}`
	- Note that the value being filter, `title`, is a function that is applied to the **item** in the **context** whose key is `django`
- And the context is:
	- ``{'django': 'the web framework for perfectionists with deadlines'}
- The result of applying the filter (and replacing the "filter expression" above) is
	- 'The Web Framework for Perfectionists with Deadlines'

Some filters can also **take arguments**
- For example
	- `{{ my_date|date:"Y-m-d" }}`
- This filter applies the `date` filter which actually formats `my_date` using the format "Y-m-d"


