from django import forms
from django.contrib.auth.models import User

# class Userform(forms.ModelForm):
#     username = forms.CharField()
#     email = forms.CharField()
#     password = forms.CharField()
#     class Meta:
#         model = User
#         fileds = ['username','email','password']

class TestForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    url = forms.URLField(required=False)
    comment = forms.CharField(required=True, widget=forms.Textarea)

