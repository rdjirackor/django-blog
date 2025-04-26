from django import forms
from .models import Post, ContactMessage

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']


class ContactForm(forms.ModelForm):
    class Meta:
        model=ContactMessage
        fields= ['first_name','last_name','email','phone_number','message']