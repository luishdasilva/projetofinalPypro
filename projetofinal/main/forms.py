from django import forms


class UserForm(forms.Form):
    Urrls = forms.URLField()
