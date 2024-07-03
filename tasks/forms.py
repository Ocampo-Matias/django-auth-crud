from django import forms
from .models import task

class TaskForm(forms.ModelForm):
    class Meta:
        model=task
        fields=['title','description','important']
        widgets={
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Write a title'}),
            'description': forms.Textarea(attrs={'class':'form-control' ,'placeholder':'Write a description'}),
            'important': forms.CheckboxInput(attrs={'class':'form-check-input ' }),
            
            
        }