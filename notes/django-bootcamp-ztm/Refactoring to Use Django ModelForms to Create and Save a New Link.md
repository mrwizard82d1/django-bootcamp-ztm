Django saves us the work of querying each form parameter 

Change our form in `forms.py`
- Inherit from `forms.ModelForm`
- Remove the "hand-defined" properties we created previously
	- `name`
	- `url`
	- `slug`
- Define a `Meta` class **within** our `LinkForm` class-
	- This class provides information **about** our properties 
	- That `ModelForm` needs to correctly render the required properties
	- Specify the `model` attribute of the embedded `Meta` class
	- Specify an array (or a tuple) of our field names

Change `views/add_link()` to take advantage of these changes
- Instead of simply printing out `forms.cleaned_data`
- We save the data
	- `form.save()`
- And return the user to the home page
	- `from django.urls import reverse`
	- `return redirect(reverse('home'))` (uses our symbolic name)

In the next video, we will:
- Improve the appearance through styling our page
- Wire up the existing "Add link" button
