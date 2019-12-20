from django import forms

class LoginPassword(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100)


class LoginFace(forms.Form):
    username = forms.CharField(label='Username', max_length=100)