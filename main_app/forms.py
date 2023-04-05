from django import forms
from main_app import models


class UploadIllustrationForm(forms.ModelForm):
    prompt = forms.CharField(label="Prompt",widget=forms.Textarea(attrs={"rows":5}))
    description = forms.CharField(label="Description",widget=forms.Textarea(attrs={"rows":5}))
    class Meta:
        model = models.IllustrationModel
        fields = ('image','tag','title','prompt','seed','description')

    def clean_image(self):
        value = self.cleaned_data['image']
        if value.name.split('.')[-1] not in ['png','jpg']:
            raise forms.ValidationError("Image must be png or jpg")
        return value


class UploadTextForm(forms.ModelForm):
    description = forms.CharField(label="Description",widget=forms.Textarea(attrs={"rows":5}),required=False)
    class Meta:
        model = models.TextModel
        fields = ('text','tag','title','description')

