from django.contrib import admin


# Register your models here.
from .models import BG,Entry #imports the BoardGame class from models.py

admin.site.register(BG) #tells Django to manage models through admin site
admin.site.register(Entry) 