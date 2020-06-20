from django.contrib import admin

# Register your models here.
from .models import Guitar, Variations, Guitarist

admin.site.register(Guitar)

admin.site.register(Variations)

admin.site.register(Guitarist)


