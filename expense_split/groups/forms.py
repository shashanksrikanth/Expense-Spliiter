from django import forms

class GroupForm(forms.Form):
    group_name = forms.CharField(max_length=200)
    members = forms.CharField(max_length=20000000000000)