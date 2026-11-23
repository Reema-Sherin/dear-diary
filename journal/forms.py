from django import forms
from .models import Achievement

class AchievementForm(forms.ModelForm):

    class Meta:
        model = Achievement
        fields = [
            'title',
            'description',
            'achieved_on',
            'photo'
        ]
        widgets = {
            'achieved_on': forms.DateInput(
                attrs={'type': 'date'}
            )
        }