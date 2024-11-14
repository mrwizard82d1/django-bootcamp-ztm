from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm


class SignupView(CreateView):
    """Supports a prospective user becoming a registered user."""
    form_class = UserCreationForm  ## form to use

    # After a user registers, we will prompt them to login
    success_url = reverse_lazy('login')

    # The template to use to render the UI
    template_name = 'registration/signup.html'


