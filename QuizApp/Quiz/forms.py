from django import forms

class submitForm(forms.Form):
    participant = forms.CharField(label ="User Name")
    quizname = forms.CharField(label="Quiz Name")


