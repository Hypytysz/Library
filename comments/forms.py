from django import forms

from comments.models import CommentPost


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentPost
        exclude = ['post']