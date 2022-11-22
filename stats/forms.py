from django import forms
from .models import Fantasy


class FantasyForm(forms.ModelForm):

    class Meta:
        model = Fantasy
        fields = ('match', 'score1', 'score2')
