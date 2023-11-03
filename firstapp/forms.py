from django import forms
from firstapp.models import Profile

class ProfileForm(forms.ModelForm):
    name=forms.CharField(label="Full Name",required=True)
    email=forms.EmailField(label="Email Address",required=True)
    phone=forms.CharField(label="Phone Number",required=True)
    class Meta:
        model=Profile
        fields=('name','email','phone','age','image','gender','religion','address')