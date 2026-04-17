from django import forms

class Form(forms.Form):
    evento = forms.CharField(label='Evento', max_length=100)
    local = forms.CharField(label='Local', max_length=100)