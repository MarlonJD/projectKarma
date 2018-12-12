from django.contrib import admin

from django.contrib import admin

from .models import *

admin.site.register(Startup)
admin.site.register(Project)
admin.site.register(Folder)
admin.site.register(Notebook)

