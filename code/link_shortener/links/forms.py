"""A module containing our Django Forms"""

from django import forms

from links.models import Link


class LinkForm(forms.ModelForm):
    """Defines a form - associated with a model - for creating a new link for our application."""

    # The base class will automatically create our form fields base on our model
    # However, we must define some `Meta` properties
    class Meta:
        model = Link
        fields = ('name', 'url', 'slug')
