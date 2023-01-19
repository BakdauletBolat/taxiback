from django import forms
from form.models import FeedBack


class FeedBackForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    email = forms.EmailField()
    text = forms.CharField()

    class Meta:
        model = FeedBack
        fields = '__all__'
