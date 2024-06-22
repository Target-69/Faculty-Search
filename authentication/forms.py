# forms.py
from django import forms

class FacultySearchForm(forms.Form):
    search_query = forms.CharField(label='Search Faculty')
