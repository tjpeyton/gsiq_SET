from django import forms

class LoginForm(forms.Form):
    camp_id = forms.IntegerField(label='Campaign Id:',widget=forms.NumberInput(attrs={'placeholder': 'e.g. "24"'}))
    camp_pass = forms.CharField(label='Password:',widget=forms.PasswordInput(attrs={'placeholder': 'password'}), max_length=100)
