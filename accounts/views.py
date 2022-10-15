from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


# https://bbbootstrap.com/snippets/individual-user-profile-social-network-94176986

# https://bootsnipp.com/snippets/K0ZmK
# https://freefrontend.com/bootstrap-profiles/


def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                return redirect("register")
    else:
        form = AuthenticationForm()

    context = {
        "form": form
    }

    return render(request, "blog/login.html", context)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    context = {
        "form": form
    }
    return render(request, 'blog/register.html', context)


@login_required
def log_out(request):
    logout(request)
    return redirect("home")
