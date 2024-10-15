
Templates are **HTML blueprints**
- Some preprocessing
- Final result is an HTML file

Templates avoid the tedium of creating each page individually
- For example, a template may contain
	- The menu
	- Blog #1 title
	- Blog #1 Content

Django Template Language
- Variables: `{{ blog_title }}` (The title of the blog)
- Tags: `{% if has_title %}` Determine if the page has a title
- Filters: `{{ blog_title|title }}` The filter `title` is applied to the variable `blog_title`

A template file is like a blueprint
- But with "substitutable pieces"

