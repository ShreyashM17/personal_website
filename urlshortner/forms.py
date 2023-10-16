from django import forms
from .models import Url


class urls(forms.ModelForm):
    link = forms.CharField(widget=forms.TextInput(attrs=
                                                  {
                                                      'class': 'size',
                                                      'placeholder': 'Enter the url here'
                                                  }
                                                  ))

    class Meta:
        model = Url
        fields = [
            'link'
        ]

    def links(self):
        link = self.cleaned_data['link']
        return link
