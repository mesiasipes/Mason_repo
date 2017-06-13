from django import forms
from django.contrib.auth.forms import AuthenticationForm

from story.models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('author','title','text')


class LoginForm(AuthenticationForm):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
