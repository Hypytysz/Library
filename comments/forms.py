from django import forms

class CommentForm(forms.Form):
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)