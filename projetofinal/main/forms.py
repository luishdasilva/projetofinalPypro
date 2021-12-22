from django import forms


class UserForm(forms.Form):
    Urls = forms.URLField()
