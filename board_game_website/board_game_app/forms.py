from django import forms

from .models import BoardGame
from .models import ReviewGame

class BoardGameForm(forms.ModelForm):
      
      class Meta:
            model = BoardGame
            fields = ['text']
            labels = {'text': ''} 

class ReviewGame(forms.ModelForm):
    class Meta:
        model = ReviewGame
        fields = ['text']
        labels = {'text': 'ReviewGame'}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}