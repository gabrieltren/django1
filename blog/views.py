from django.shortcuts import render

from .models import Post
# Create your views here.

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
    