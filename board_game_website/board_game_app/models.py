from django.db import models # models tell Django how to work with data that is stored in the app

# Create your models here.

class BG(models.Model):
    """Board games that can be lent to others."""
    text = models.CharField(max_length=200) #Name of the board game
    date_added = models.DateTimeField(auto_now_add=True) #When the board game has been added to the database.

    def __str__(self):
        """Returns a strin representation of model."""
        return self.text #return the text as a string

class Entry(models.Model):
    """Currently avaiable board games."""

    bg = models.ForeignKey(BG, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        return f"{self.text[:50]}..."