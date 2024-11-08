from django.core.validators import MaxValueValidator
from django.db import models

from django.contrib.auth import get_user_model

# Create your models here.

# In this project we will use two tables:
# - Trips
# - Notes (associated with a trip)
#   - Notes may include **images**

class Trip(models.Model):
    # Who is the currently logged-in user?
    User = get_user_model()

    city = models.CharField(max_length=50)

    # The country uses a two-character code
    country = models.CharField(max_length=2)
    # The start and end dates can be "empty"; that is,
    # Neither `start_date` nor `end_date` is required
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    # The `User` must be known to the application and is a
    # **foreign key** in our model; that is, a "link" to
    # another entity in another table.
    # In addition, setting the `related_names` parameter to
    # `trips`  means that one can query **all** the trips
    # of an authenticated user.
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')

    def __str__(self):
        """Return a human-readable representation of this trip."""
        return self.city

class Note(models.Model):
    """Models a note about a trip."""

    # Valid excursions for the `type` attribute.
    EXCURSIONS = (
        ("event", "Event"),
        ("dining", "Dining"),
        ("experience", "Experience"),
        ("general", "General"),
    )

    # A note is for exactly one `Trip`
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='notes')

    # Briefly identifies this `Note`
    name = models.CharField(max_length=100)

    # A more detailed description of this note
    description = models.TextField()

    # The type of the event
    type = models.CharField(max_length=100, choices=EXCURSIONS)

    # We may want to store a picture
    # Using a parent directory of 'notes' will create a directory
    img = models.ImageField(upload_to='notes', blank=True, null=True)

    # Rate whatever this `Note` is about
    rating = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(5)])

    def __str__(self):
        """The human-readable representation of this note."""
        return f'{self.name} in {self.trip.city}'
