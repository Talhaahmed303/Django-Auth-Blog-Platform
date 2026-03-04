from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm

# List all published blogs
def blog_list(request):
    blogs = Blog.objects.filter(status='published').order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

# Blog detail
def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug, status='published')
    return render(request, 'blog/blog_detail.html', {'blog': blog})

# Create blog
@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_detail', slug=blog.slug)
    else:
        form = BlogForm()
    return render(request, 'blog/blog_form.html', {'form': form})

# Edit blog
@login_required
def blog_edit(request, slug):
    blog = get_object_or_404(Blog, slug=slug, author=request.user)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', slug=blog.slug)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/blog_form.html', {'form': form})

# Delete blog
@login_required
def blog_delete(request, slug):
    blog = get_object_or_404(Blog, slug=slug, author=request.user)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, 'blog/blog_confirm_delete.html', {'blog': blog})