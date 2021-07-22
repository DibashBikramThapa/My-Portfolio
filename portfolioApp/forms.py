from django import forms
from portfolioApp import models


class ProfileForm(forms.ModelForm):
    class Meta:
        model=models.Profile
        fields=['profilepic','text','company','address']


class AboutMeForm(forms.ModelForm):
    class Meta:
        model=models.AboutMe
        fields=['text',]
