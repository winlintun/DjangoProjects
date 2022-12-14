from django import forms
from .models import Blog, Comment


class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = ["title", "body", "image", "status", 'tag']

	def __init__(self, *args, **kwargs):
		super(BlogForm, self).__init__(*args, **kwargs)

		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'
		
		if self.fields['tag'] and self.fields['status'] and self.fields['image']:
			self.fields['tag'].widget.attrs['class'] = 'form-select'
			self.fields['status'].widget.attrs['class'] = 'form-select'
			self.fields['image'].widget.attrs['class'] = 'input-group-text'

		self.fields['image'].widget.attrs['accept'] = "image/png, image/gif, image/jpeg"
		# self.fields['upload_book'].widget.attrs['accept'] = '.pdf'


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ["name", "email", "body"]

	def __init__(self, *args, **kwargs):
		super(CommentForm, self).__init__(*args, **kwargs)

		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'
