from django import forms
from .models import Side

class SideForm(forms.ModelForm):
    class Meta:
        model = Side
        fields = ['drinks', 'starter']