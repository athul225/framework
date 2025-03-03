from django import forms


class user_forms(forms.Form):
    roll=forms.IntegerField()
    name=forms.CharField()
    mark=forms.IntegerField()