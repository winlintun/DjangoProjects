from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


STATUS = (
	(0, 'Draft'),
	(1, "Publish")
)

class Post(models.Model):
	title = models.CharField(max_length=200, blank=False, null=False)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	slug = models.SlugField(blank=False, null=False)
	update_date = models.DateTimeField(auto_now=True)
	content = models.TextField(blank=True, null=True)
	image = models.ImageField(upload_to="media", blank=True, null=True)
	created_date = models.DateTimeField(default=timezone.now)
	status = models.IntegerField(choices=STATUS, default=0)


	def __str__(self):
		return self.title



class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	email = models.EmailField()
	body = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=False)

	def __str__(self):
		return "Comment: {} -> {}".format(self.name, self.post.title)



