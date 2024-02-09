from django import forms
from .models import Lecture, Course

class TimetableForm(forms.ModelForm):
  
    class Meta:
        model = Lecture
        fields = ['course','professor', 'classroom', 'name','day', 'start_time', 'end_time']
        widgets = {
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }
