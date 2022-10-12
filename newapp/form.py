
from django import forms

class urlform(forms.Form):
    url = forms.CharField(label='ENTER URL', max_length=1024)