from django import forms
'''
Created on 2014Äê3ÔÂ30ÈÕ

@author: liyi
'''

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False) message = forms.CharField()