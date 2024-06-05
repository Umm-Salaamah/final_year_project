from django import forms

class URLForm(forms.Form):
    url = forms.URLField(label='Enter URL to scan', max_length=200)
