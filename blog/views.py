from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Post
# Create your views here.
@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/')

def login_user(request):

    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'login.html')

def login_submit(request):
    print(request.POST)
    if request.POST:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user =authenticate(username=usuario, password=senha)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuario ou senha invalida')
            return render(request, 'login.html')
        
    else:
        messages.error(request, "Erro Ao logar")
        return render(request, 'login.html')

def index(request):
    
    post = Post.objects.all()
    
    context = {
        'post': post
    }
    return render(request, 'index.html', context)

def item_post(request, id):
    post = Post.objects.get(id=id)
    
    context = {
        'post': post
    }
    return render(request, 'item_post.html', context)
    