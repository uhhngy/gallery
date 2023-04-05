from django import forms
from django.core.validators import MinLengthValidator

class ImagePromptForm(forms.Form):
    apikey = forms.CharField(
            label='API Key:',
            validators=[MinLengthValidator(10, message="Please enter your api key.")],
            max_length=100,
        )
    prompt = forms.CharField(
            label='',
            validators=[MinLengthValidator(10, message="Please enter at least 10 characters.")],
            max_length=100,
            widget=forms.Textarea(attrs={"rows":5, "placeholder": "Enter your text prompt here"}),
        )
    size_choices = [
        ('256x256', '256x256'),
        ('512x512', '512x512'),
        ('1024x1024', '1024x1024')
    ]
    size = forms.ChoiceField(choices=size_choices, initial='256x256', label='Select size')