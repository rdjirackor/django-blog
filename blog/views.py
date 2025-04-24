from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')  
    else:
        form = PostForm()
    
    return render(request, 'create_post.html', {'form': form})

def update_post(request, pk):
    post=get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = PostForm(instance=post)
    return render(request, 'update_post.html', {'form': form})

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':  # Confirm delete
        post.delete()  # Delete the post
        return redirect('main')  # Redirect to the list of posts after deletion
    
    return render(request, 'post_delete.html', {'post': post})




def main(request):
    template=loader.get_template('index.html')
    posts=Post.objects.all()
    posts.order_by('-created_at')
    context={
        'posts':posts,
    }
    return HttpResponse(template.render(context,request))

