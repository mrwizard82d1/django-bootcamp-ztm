Now make the view for the `Profile`
- We could make this a class-based view
- But we will actually make this view a function-based view

Add to `views.py`
- A function named `profile_view`
	- Takes 
		- A `request`
		- A `profile_slug`
	- Calculates the profile of the user (based on `profile_slug`)
	- Gets **all** the links associated with this profile
		- Thanks to our `ForeignKey` 
		- With its `related_name` parameter

Configure the URL for the view
- Add to `urlpatterns`
	- `path('<slug:profile_slug>', profile_view, name='profile')`
	- Remember that `profile_view` as a **function-based view**

Create `profile.html`
- Copied [from link](https://github.com/vacchiano/ZTM-Django-cbv/blob/master/link_plant/templates/link_plant/profile.html)
- Includes the `tailwind` script
- "Injects" the `profile.bg_color` into a class string using `{{}}`
- Loop through each link in the profile
	- Display each link as a button

Update `link_list.html`
- To allow navigation to the profile 

	