from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'you@example.com'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'How can I help?'}))
