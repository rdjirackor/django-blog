from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Post
from .forms import PostForm,ContactForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required



def custom_logout_view(request):
    logout(request)
    return redirect('/')
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')  
    else:
        form = PostForm()
    
    return render(request, 'create_post.html', {'form': form})
@login_required
def update_post(request, pk):
    post=get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = PostForm(instance=post)
    return render(request, 'update_post.html', {'form': form,})
@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':  
        post.delete()  
        return redirect('main')  
    
    return render(request, 'post_delete.html', {'post': post})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'template.html', {'form': ContactForm(), 'message_sent': True})  
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

def aboutMe(request):
    return render(request, 'about_me.html')

def aboutBlog(request):
    return render(request, 'about_blog.html')

def notFound(request):
    return render(request, '404.html')

def main(request):
    template=loader.get_template('index.html')
    posts=Post.objects.all()
    posts.order_by('-created_at')
    context={
        'posts':posts,
    }
    return HttpResponse(template.render(context,request))

