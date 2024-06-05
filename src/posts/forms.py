from django import forms

from .models import InstagramVideoPostModel


class InstagramVideoPostURLForm(forms.Form):
    url = forms.URLField(label="Post URL")


class InstagramVideoPostShortForm(forms.ModelForm):
    class Meta:
        model = InstagramVideoPostModel
        fields = ("view_count", "likes_count", "comments_count")
