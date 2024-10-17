Template inheritance (from Django docs)
- Most powerful
- And most complex part of Django's template engine
- Allows one to build a "skeleton" template containing common elements
- But defines **block** that can be overridden by **child** templates

Review of Django [template inheritance example](https://docs.djangoproject.com/en/5.1/ref/templates/language/#template-inheritance)
- Consists of a parent template, typically called something similar to`base.html`
- Base - or parent - defines **blocks** with content that
	- Derived - or child - templates can **override**
- The child template **need not** define the complete page
	- But only the blocks it wishes to override
- If a child template **does not** override a block, 
	- The HTML from the parent (or base) template is used

Not limited to a single level of inheritance

Gotchas / Tips
- If you use `{% extends <template-name-string> %}` it must be the **first** template tag in the template; otherwise, template inheritance **will not work**
- Generally better to have **more** block tags in `base` HTML than less
	- If you find yourself duplicating code in a number of derived templates, consider moving that content to a `{% block %}`in the base/parent template
- The "variable" `{{ block.super }}` allows one to access the **content** of the parent template
	- Be wary of escaped data in the parent block
- Variable created **outside** the `{% block ... %}` using the template `as` syntax **cannot** be used inside the block
	- The following template will not render anything:
```python
{% translate "Title" as title %}
{% block content %}{{ title }}{% endblock %}
```

