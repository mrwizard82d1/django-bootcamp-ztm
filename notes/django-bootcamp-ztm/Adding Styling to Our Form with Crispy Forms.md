Our functionality all appears to be working. Onto styling.

We will use an existing library, `django-crispy-forms`.
- A popular package
- Template packs
	- Allow one to add styling based on existing CSS framework

Typical steps
- Stop server
- Atypical
	- Shutdown PyCharm (see [JetBrains YouTrack page](https://youtrack.jetbrains.com/issue/PY-65945/PyCharm-cant-delete-revert-changes-in-pyproject.toml-with-Poetry-section))
	- Navigate to a terminal
	- Execute `poetry add django-crispy-forms`
	- Re-open PyCharm and this project
- Add `crispy-forms` to 'INSTALLED_APPS'
	- Because we are using "Tailwind", we must install an additional package, `crispy-tailwind`
	- And we must add `crispy-tailwind` to 'INSTALLED_APPS'
		- And we must add two additional variables to `settings.py`
			- `CRISPY_ALLOWED_TEMPLATE_PACKS = 'tailwind'`
			- `CRISPY_TEMPLATE_PACK = 'tailwind'`
- Change  `create.html` page
	- After `extend`
		- `{% load tailwind_filters %}`
	- Apply the `cripsy` filters to `form`
		- `{{ form|crispy }}`

In the next section, we will look at class-based views (instead of functional-based)


