from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def index(request):
    """index page"""
    ctx = {
    }

    if request.user.is_authenticated:
        username = request.user.username
        user = request.user
        ctx['userobj'] = user

        return render(request, 'index.html', ctx)
    else:
        return redirect('login')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def interest(request):
    ctx = {
    }

    return render(request, 'interest.html', ctx)
