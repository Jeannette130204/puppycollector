from django.contrib import admin

from .models import Puppy, Walkings, Clothes

admin.site.register(Puppy)
admin.site.register(Walkings)
admin.site.register(Clothes)

# Register your models here.
