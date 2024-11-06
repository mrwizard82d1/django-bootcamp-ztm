We will use Crispy Forms and Crispy-Tailwind for styling
- The [project source page](https://github.com/django-crispy-forms/crispy-tailwind) describes the installation steps
- Pre-requisite
	- Shutdown running application

Install `crispy-tailwind`
- `pip install crispy-tailwind`

Install two apps
- `crispy_forms`
- `crispy_tailwind`

Specify the appropriate template packs
- `CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"`
- `CRISPY_TEMPLATE_PACK = "tailwind"`

Use crispy forms and crispy tailwind in pages
- Edit `link_plant/templates/link_plant/link_form.html`
- Load `tailwind_filters`

Test changes
- Restart application
- Navigate to `link/create`
	- Verify that the form is now styled (looks better)



