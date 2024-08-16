from django import forms
from .models import ScheduledScan

class ScheduledScanForm(forms.ModelForm):
    class Meta:
        model = ScheduledScan
        fields = ['url', 'interval']

class URLForm(forms.Form):
    url = forms.URLField(label='Enter URL to scan', max_length=200)
