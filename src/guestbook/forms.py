from django import forms 

class ReviewForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(required=False)
    entry = forms.CharField(widget=forms.Textarea)