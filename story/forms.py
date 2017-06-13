from django import forms
from story.models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('author','title','text')
