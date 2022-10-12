from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, CommentForm, PostEditForm
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models import Q


def home(request):
	post = Post.objects.filter(status=True).order_by('-created_date')

	context = {
		'posts': post
	}

	return render(request, 'blog/home.html', context)


def detail(request, pk, slug):
	post = Post.objects.get(id=pk)
	slug = post.slug == slug

	comment = post.comment_set.filter(active=True)
	new_comment=None
	if request.method == "POST":
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.post = post
			new_comment.save()
	else:
		comment_form = CommentForm()


	context = {
		"post": post,
		"slug": slug,
		'comment_form': comment_form,
		'comment': comment,
		"new_comment":new_comment
	}

	return render(request, "blog/detail.html", context)


def create(request, pk):
	user = User.objects.get(id=pk)

	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			title = form.cleaned_data['title']
			author = user
			slug = slugify(title)
			content = form.cleaned_data['content']
			created_date = form.cleaned_data['created_date']
			status = form.cleaned_data['status']
			image = form.cleaned_data['image']

			post = Post.objects.create(title=title, author=author, slug=slug, content=content, image=image, created_date=created_date, status=status)
			post.save()

			return redirect("home")
	else:
		form = PostForm()

	context = {
		'form': form
	}

	return render(request, "blog/create.html", context)


def edit(request, pk):
	post = Post.objects.get(id=pk)

	if request.method == "POST":
		edit = PostEditForm(request.POST, request.FILES, instance=post)
		if edit.is_valid():
			edit.save()
			return redirect("home")
		#print("form in: ", edit)
	else:
		edit = PostEditForm(instance=post)
		#print("form out: ", edit)

	context = {
		"edit": edit
	}

	return render(request, "blog/edit.html", context)



def search(request):
	if request.method == "GET":
		query  = request.GET['q']

		if query is not None:
			result = Post.objects.filter(Q(title__contains=query))

	context = {
		"result": result
	}

	return render(request, "blog/search.html", context)

def delete(request, pk):
	post = Post.objects.get(id=pk)
	post.delete()
	return redirect("home")