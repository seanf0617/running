from django import forms
from .models import RecordActivity

class RecordActivityForm(forms.ModelForm):
    class Meta:
        model = RecordActivity
        fields = ['date', 'distance']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }