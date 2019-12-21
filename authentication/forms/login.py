from django import forms

class LoginPassword(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100)

class LoginFace(forms.Form):
    username = forms.CharField(label='Username', max_length=100)

class Register(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100)
    wallet = forms.CharField(label='WalletID', max_length=100)
    pk = forms.CharField(label='PrivateKey', max_length=100)