from django import forms
from .models import JobApplication

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        exclude = ('status','applied_for',)
