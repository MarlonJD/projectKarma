from django import forms
from django.forms import ModelForm
from .models import Startup


class TeamForm(ModelForm):
    name = forms.CharField(max_length=100, label="Team Name")
    perma = forms.SlugField(max_length=20, label="Team Perma-Link", help_text="It's your team's perma-link adress. e.g. 'Example Company' should be 'example-company' or 'example_company' or 'examplecompany'")
    class Meta:
        model = Startup
        fields = ['name', 'perma']