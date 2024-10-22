
Output is not "friendly"
- Will use `django.contrib.humanize`
- Distributed with `django`
- But **not** installed by default
- "A set of Django template filters useful for adding a 'human touch to data."

Add `django.contrib.humanize` to `settings.py`

Load `humanize` to add these filters

Apply filters to output
- `posting.title|title` - display in title case
- `posting.description|capfirst` - capitalize first word
- `posting.salary|intcomma` - insert comma numeric separators

Our next step, display all the details of a selected job



