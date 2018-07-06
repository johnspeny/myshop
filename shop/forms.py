from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message..'}))
	sender = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))