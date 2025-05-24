from django import forms
from .models import Users

class Userregistration(forms.ModelForm):
    class meta:
        Model=Users
        fields=['Firstname','lastname','email','password','phone']

