from django.shortcuts import render, redirect
from .forms import BlogForm, CommentForm
from django.contrib import messages
from .models import Blog, Comment, CustomUser

def homepage(request):
    posts = Blog.objects.all().order_by('-date').prefetch_related('comments').select_related('author')
    return render(request, 'index.html', {'posts':posts})

def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            messages.add_message(request, messages.SUCCESS, 'Blog muvaffaqiyatli qo\'shildi.')
        else:
            messages.add_message(request, messages.ERROR, form.errors)

    return render(request, 'add-post.html')


def add_comment(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog_id = request.POST.get('blog')
            comment.author = request.user
            comment.save()

    return redirect(request.META.get('HTTP_REFERER'))
        
def filter_by_author(request, author):
    if not author:
        posts = Blog.objects.order_by('-date').prefetch_related('comments').select_related('author')
    else:
        posts = Blog.objects.order_by('-date').prefetch_related('comments').select_related('author').filter(author__id=author)
    
    authors = CustomUser.objects.all()
    default_author = CustomUser.objects.filter(id=author)

    return render(request, 'filter-author.html', {'posts': posts, 'authors': authors, 'default_author': default_author})

