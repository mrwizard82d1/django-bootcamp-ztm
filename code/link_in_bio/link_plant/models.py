from django.db import models

# Create your models here.

# Remember, each class is a **table** in our database.
# Our system contains two models:
# - Profiles
# - Links (related to Profiles)

class Profile(models.Model):
    """Models the profile of a single user."""

    BG_CHOICES = (
        # database valuable, human-readable value
        ("blue", "Blue"),
        ("green", "Green"),
        ("yellow", "Yellow"),
    )
    # We will probably want:
    # - name (of the profile)
    # - slug (a URL friendly version of the name)
    # - bg_color (background color for this profile)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    bg_color = models.CharField(max_length=50, choices=BG_CHOICES)

    def __str__(self):
        """Return string representation (for people) of the model."""
        return self.name


class Link(models.Model):
    """Models a link used in a profile."""
    # text. unl, profile
    text = models.CharField(max_length=100)
    url = models.URLField()
    # Secondary key relating many link to one profile
    # Many links to **one** profile
    # `related_name` parameter identifies the **table** whose key (ID)
    # identifies a related `Profile`; that is, supports reverse links
    profile = models.ForeignKey(Profile,
                                on_delete=models.CASCADE, related_name='links')
