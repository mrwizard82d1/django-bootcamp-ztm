"""A module containing our Django Forms"""

from django import forms


class LinkForm(forms.Form):
    """Defines a form for creating a new link for our application."""

    # Like with a `Model`, we define input form elements by adding class members.
    name = forms.CharField(max_length=50)
    url = forms.URLField(max_length=200)
    slug = forms.SlugField(required=False)

