from django.db import models
from django.utils.text import slugify


# Create your models here.
class Link(models.Model):
    """Save a shortened link into the database.

    The database might contain the following fields:
    - name
    - url
    - slug
    - number of clicks
    """
    name = models.CharField(max_length=50, unique=True)
    # Capture the full length our short link replaces.
    url = models.URLField(max_length=200)
    # A "slug" is a newspaper term. We use it to provide
    # a more user-friendly but short URL.
    # Setting the option, `blank=True`
    slug = models.SlugField(unique=True, blank=True)
    # The number of clicks
    clicks = models.PositiveIntegerField(default=0)

    def __str__(self):
        """Return a human-friendly string for this model."""
        return f"{self.name} ({self.clicks})"

    # Define methods for common actions
    def click_count(self):
        """Increment the number of clicks on this link."""
        self.clicks += 1
        self.save() # saves the updated state

    def save(self, *args, **kwargs):
        """Override the `save()` method to save the link.

        As a "side effect," generate a slug of none supplied.

        args - Additional positional parameters.
        kwargs - Additional keyword parameters.
        """
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)
