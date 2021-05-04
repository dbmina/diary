from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    if request.method == 'GET': # index
        posts = Post.objects.all()
        return render(request, 'diary/index.html', {'posts': posts})
    elif request.method == 'POST': # create(form을 이용하여 submit한 형태) 
        title = request.POST['title']
        satisfaction = request.POST['satisfaction']
        content = request.POST['content']
        Post.objects.create(title=title, satisfaction=satisfaction, content=content)
        return redirect('diary:index') 

def create(request):
    return render(request, 'diary/create.html')

def show(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'diary/show.html', {'post':post})

def edit(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'diary/edit.html', {'post':post})

def update(request, id):
    title =request.POST.get('title')
    content =request.POST.get('content')
    satisfaction=request.POST.get('satisfaction')
    Post.objects.filter(id=id).update(title=title, satisfaction=satisfaction, content=content)
    return redirect(f'/post/{id}/')

def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete() 
    return redirect('diary:index')