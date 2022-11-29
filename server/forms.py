from django import forms

class buttonForm(forms.Form):
    btn = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
