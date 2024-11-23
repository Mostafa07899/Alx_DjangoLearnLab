from django import forms


class ExampleForm(forms.Form):
    query = forms.CharField(max_length=200, required=False)