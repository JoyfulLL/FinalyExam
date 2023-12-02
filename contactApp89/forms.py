from django import forms
from .models import Resume


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('name', 'experience', 'photo')
        widgets = {
            'photo': forms.FileInput(),
        }
