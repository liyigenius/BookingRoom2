from django import forms
'''
Created on 2014��3��30��

@author: liyi
'''

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False) message = forms.CharField()