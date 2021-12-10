from django.contrib import admin


# Register your models here.
from .models import BoardGame, ReviewGame #imports the BoardGame class from models.py

admin.site.register(BoardGame) #tells Django to manage models through admin site
admin.site.register(ReviewGame)