
Create `triptrak/views.py`
- Import a number of functions and classes
	- `django.uls.reverse_lazy`
	- `django.views.generic.CreateView`
	- `django.contrib.auth.forms.UserCreationForm`

Create class `SignupView(CreateView)`
- Remember "form class"
- Calculate the URL to which to navigate when successfully registered
- Set the template to be used to render this view

Edit `triptrak/urls.py`
- Map `accounts/signup` to `SignupView.as_view()`

Create the template
- Add file `templates/registration/signup.html`
- Add header
- Add form
	- Action: `{% url 'signup' %}`
	- Method "POST"
	- Include 
		- `{% csrf_token %}`
		- `{{ form.as_p }}``
		- Submit button