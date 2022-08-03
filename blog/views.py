from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post

from .forms import CreateUserForms, PostModelForm
# Create your views here.

@login_required(login_url='/login/')
def post_registre(request):
    if request.method == 'POST':
        if request.POST:
            form = PostModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/')
            else:
                messages.error(request, 'Erro ao salvar post')
            context = {'form': form}    
            return render(request, 'post_registre.html', context=context)
        else:
            return redirect('/')
    else:
        form = PostModelForm()
        context = {'form': form}    
        return render(request, 'post_registre.html', context=context)

def registre(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = CreateUserForms(request.POST)
        if form.is_valid():
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                user = User.objects.create(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    first_name=form.cleaned_data['first_name']
                )
                user.set_password(form.cleaned_data['password1'])
                user.save()
                login(request, user)
                return redirect('/')
                    
            else:
                messages.error(request, 'Senhas nao são iguais')    
        else:
            messages.error(request, 'Erro ao criar registro')
        
        context ={
            "form": form
        }
        return render(request, 'registre.html', context)   
    else:
        form =CreateUserForms()
        context ={
            "form": form
        }
        return render(request, 'registre.html', context)

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
    