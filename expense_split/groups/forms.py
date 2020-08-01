from django import forms

class GroupForm(forms.Form):
    group_name = forms.CharField(max_length=200)
    members = forms.CharField(max_length=20000000000000)
    password = forms.CharField(max_length=200)

class EmailForm(forms.Form):
    group_name = forms.CharField(max_length=200)
    amount = forms.IntegerField()
    reason = forms.CharField(max_length=1000)
    password = forms.CharField(max_length=200)

class DeleteForm(forms.Form):
    group_name = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)