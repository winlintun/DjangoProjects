from django.shortcuts import render, redirect
from .models import Blog, Tag, Comment
from .forms import BlogForm, CommentForm
from django.contrib.auth.models import User
from django.utils.text import slugify
from random import shuffle
from django.db.models import Q
# Create your views here.


def popular():

	top_post = Blog.objects.all().order_by("-created_date")[:5]
	return top_post


def item_count():
	tag = Tag.objects.all()

	tags = {}

	for j in tag:
		tag_id = j.id
		tags[j] = Tag.objects.get(id=tag_id).blog_set.all().count()
	
	return tags


def home(request, pk):

	user = User.objects.get(id=pk)
	blog = Blog.objects.filter(author=user).order_by('-created_date')
	draft = blog.filter(status=1)

	context = {
		'blog': draft,
		"top_post": popular(),
		'tags': item_count(),
		'drafts': draft,
	}

	return render(request, 'blog/index.html', context)


def detail(request, pk, slug):
	blog = Blog.objects.get(id=pk)
	if blog.slug == slug:
		pass

	comment = blog.comment_set.filter(active=True)
	new_comment = None

	if request.method == "POST":
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.blog = blog
			new_comment.save()
	else:
		comment_form = CommentForm()

	context = {
		'blog': blog,
		"top_post": popular(),
		'tags': item_count(),
		"comment": comment,
		"new_comment": new_comment,
		"comment_form": comment_form,
	}

	return render(request, 'blog/detail.html', context)


def blog_explorer(request, pk):
	user = User.objects.get(id=pk)
	blog = Blog.objects.filter(author=user)
	draft = blog.filter(status=0)

	if request.method == "POST":
		form = BlogForm(request.POST, request.FILES)

		if form.is_valid():
			title = form.cleaned_data['title']
			author = user
			slug = slugify(title)
			body = form.cleaned_data['body']
			tags = form.cleaned_data['tag']
			image = form.cleaned_data['image']
			status = form.cleaned_data['status']

			post = Blog.objects.create(title=title.title(), author=author, slug=slug, body=body, image=image, status=status)

			for i in tags:
				post.tag.add(i)
				post.save()
			return redirect("home")
	else:
		form = BlogForm()

	context = {
		"form": form,
		"drafts": draft,
	}

	return render(request, 'blog/explorer.html', context)


def feed(request):

	blog = Blog.objects.filter(status=1).order_by('-created_date')

	posts = []

	for i in blog:
		posts.append(i)

	shuffle(posts)

	context = {
		"top_post": popular(),
		'tags': item_count(),
		"posts": posts,

	}

	return render(request, 'blog/feed.html', context)


def about(request):

	return render(request, 'blog/about.html')


def contact(request):

	return render(request, 'blog/contact.html')


def single(request, user):
	user = User.objects.get(username=user)

	context = {
		"top_post": popular(),
		'tags': item_count(),
		'users': user,

	}

	return render(request, 'blog/single.html', context)


def post_edit(request, userId, postId):
	user = User.objects.get(id=userId)
	blog = Blog.objects.get(id=postId)
	if request.method == "POST":
		form = BlogForm(request.POST, request.FILES, instance=blog)

		if form.is_valid():
			form.save()
			return redirect("home")
	else:
		form = BlogForm(instance=blog)

	context = {
		"form": form
	}

	return render(request, 'blog/explorer.html', context) 


def post_delete(request, pk, slug):
	blog = Blog.objects.get(id=pk)

	blog.delete()

	return redirect("home")


def search_post(request):

	if request.method == "GET":
		queryset = request.GET.get('q')
		if queryset is not None:
			result = Blog.objects.filter(Q(title__icontains=queryset))
	context = {
		"result": result,
	}

	return render(request, 'blog/search.html', context)
