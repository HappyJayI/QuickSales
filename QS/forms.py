from django import forms
from django.contrib.auth.models import User
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = InvoiceM
        fields = ('InOutNo','InOutDate','CustSeq')

class BillForm(forms.ModelForm):
    class Meta:
        model = BillM
        fields = ('InOutNo','InOutDate','CustSeq')

class TestForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    url = forms.URLField(required=False)
    comment = forms.CharField(required=True, widget=forms.Textarea)



# class Userform(forms.ModelForm):
#     username = forms.CharField()
#     email = forms.CharField()
#     password = forms.CharField()
#     class Meta:
#         model = User
#         fileds = ['username','email','password']