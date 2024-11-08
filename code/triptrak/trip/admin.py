from django.contrib import admin

from .models import Trip, Note

# Register your models here.
# PyCharm suggested one could supply a list of models; however, nothing
# in the documentation seems to suggest that this argument type is
# supported.
admin.site.register(Trip)
admin.site.register(Note)
