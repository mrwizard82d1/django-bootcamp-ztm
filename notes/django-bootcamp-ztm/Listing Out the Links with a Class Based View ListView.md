Dive into our first class-based view

List out all our links
- Edit `link_plant/views.py`
- Include `django.views.generic.ListView`
- Include `Profile` and `Link`

Create view
	- Add `class LinkListView(ListView)`
	- Only need to specify `model = Link` in class definition
	- `ListView` class provides the "same" implementation as our function-based implementation
```python
links = Link.object.all()
context = {'links': links}
return render(request, 'link_list.html, context)
```
Add URL pattern:
- `path('', include('link_plant.urls')`

Create `link_plant/urls.py`
- Import `path`
- Import newly created view, `LinkListView`
- Add `path()` to `urlpatterns` list
	- `path('', LinkListView.as_view(), name='link-list')`
		- Since `LinkListView` is a **class**
		- We **must** invoke `as_view()` to identify the view

Create template
- Create `link_plant/templates/link_plant` directory
- Create `link_list.html` in that directory
- The `.html` file simply loops over all items in `object_list`
- And renders the text of each `link`



