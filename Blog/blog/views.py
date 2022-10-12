from django.shortcuts import render, redirect
from .models import Blog, Tag
from .forms import BlogForm
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your views here.


def popular():

	top_post = Blog.objects.all().order_by("-created_date")[:5]
	return top_post



def home(request):

	blog = Blog.objects.all()
	tags = Tag.objects.all()

	for i in tags:
		print(i)

	context = {
		'blog': blog,
		"top_post": popular(),
		'tags': tags,
	}

	return render(request, 'blog/index.html', context)



def detail(request, pk, slug):
	blog = Blog.objects.get(id=pk)


	context = {
		'blog': blog,
		"top_post": popular()
	}

	return render(request, 'blog/detail.html', context)



def blog_explorer(request, pk):
	myuser = User.objects.get(id=pk)

	if request.method == "POST":
		form = BlogForm(request.POST, request.FILES)

		if form.is_valid():
			title = form.cleaned_data['title']
			author = myuser
			slug = slugify(title)
			body = form.cleaned_data['body']
			tags = form.cleaned_data['tag']
			image = form.cleaned_data['image']
			status = form.cleaned_data['status']

			post = Blog.objects.create(title=title, author=author, body=body, image=image, status=status)

			for i in tags:
				post.tag.add(i)
				print(i)
				post.save()

			#post.save()
			return redirect("home")
	else:
		form = BlogForm()

	context = {
		"form": form
	}



	return render(request, 'blog/explorer.html', context)


def feed(request):
	
	context = {
		"top_post": popular(),

	}

	return render(request, 'blog/feed.html', context)


def about(request):
	

	return render(request, 'blog/about.html')


def contact(request):
	

	return render(request, 'blog/contact.html')


def single(request):
	

	return render(request, 'blog/single.html')