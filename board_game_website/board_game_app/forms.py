from django import forms

from .models import Boardgame

 class BoardGameForm(forms.ModelForm):
       class Meta:
            model = Topic
            fields = ['text']
            labels = {'text': ''} 


