from django import forms

class Transaction(forms.Form):
    receiver = forms.CharField(label='Receiver', max_length=100)
    private_key = forms.CharField(label='Private key', max_length=100)
    amount = forms.CharField(label='Amount', max_length=100)
