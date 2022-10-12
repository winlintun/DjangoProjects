from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Blog(models.Model):

	STATUS_CHOICE = (
		(0, 'Draft'),
		(1, "Publish")
	)

	title = models.CharField(max_length=200)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	slug = models.SlugField()
	created_date = models.DateTimeField(default=timezone.now)
	body = models.TextField(null=True, blank=True)
	updated_date = models.DateTimeField(auto_now=True)
	tag = models.ManyToManyField("Tag")
	image = models.ImageField(upload_to="images", null=True, blank=True)
	status = models.IntegerField(choices=STATUS_CHOICE, default=0)



	def __str__(self):
		return self.title



class Tag(models.Model):
	name = models.CharField(max_length=200)


	def __str__(self):
		return self.name