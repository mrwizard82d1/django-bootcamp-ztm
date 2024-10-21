from django.db import models

# Create your models here.
class JobPosting(models.Model):
    """Models a single job posting."""

    # Remember that our table will also have an `id` field
    # This field will be of type integer, will be
    # increasing, and will be automatically populated.
    title = models.CharField(max_length=100)
    # `TextField` supports a "longer string"
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
