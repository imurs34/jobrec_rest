from django.contrib import admin
from .models import Job, Ints, User

# Register your models here.
myModels = [Job, Ints, User]
admin.site.register(myModels)
