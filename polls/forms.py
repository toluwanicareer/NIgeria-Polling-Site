from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
	class Meta:
		model=ContactMessage
		fields=('email','name','message')
