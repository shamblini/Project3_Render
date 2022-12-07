from django import forms

class buttonForm(forms.Form):
    btn = forms.CharField()

class numForm(forms.Form):
    btn = forms.DecimalField()