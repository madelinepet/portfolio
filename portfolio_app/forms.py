from django.forms import ModelForm
from django import forms
from .models import Image


class ImageForm(ModelForm):
    url = forms.CharField(required=False)

    class Meta:
        model = Image
        fields = ['url']

    def __init__(self, *args, **kwargs):
        """Initializes image form
        """
        username = kwargs.pop('username')
        super().__init__(*args, **kwargs)
        self.fields['url'].queryset = Image.objects.filter(user__username=username)
