from django import forms


class LeadForm(forms.Form):
    first_name = forms.CharField(label='Enter First name', max_length=50, widget=forms.TextInput()),
    last_name = forms.CharField(label='Enter Last name', max_length=50, widget=forms.TextInput()),
    email = forms.EmailField(label='Enter Email address', max_length=50, widget=forms.EmailInput()),
