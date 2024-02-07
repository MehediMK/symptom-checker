from django import forms
from .models import Symptom

class SymptomCheckForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')], widget=forms.RadioSelect)
    age = forms.IntegerField()
    symptoms = forms.MultipleChoiceField(choices=[(symptom.id, symptom.name) for symptom in Symptom.objects.all()], widget=forms.CheckboxSelectMultiple)
