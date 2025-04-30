from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseServerError
from .models import Post, Tag, Upvote, Comment

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'Invalid credentials')
            return render(request, 'login.html')
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            messages.error(request, 'Please fill in all fields')
            return render(request, 'signup.html')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is taken')
            return render(request, 'signup.html')
        User.objects.create_user(username=username, password=password)
        messages.success(request, 'User created successfully')
        return render(request, 'signup.html')
    return render(request, 'signup.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('homepage')
    return redirect('homepage')

def homepage(request):
    posts = Post.objects.all().order_by('-created_at')[:10]
    return render(request, 'index.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        tags = request.POST.get('tags')
        post = Post.objects.create(
            user=request.user,
            title=title,
            content=content
        )
        if tags:
            for tag in tags.split(','):
                Tag.objects.create(post=post, tag=tag.strip())
        return redirect('post_detail', post_id=post.id)
    return render(request, 'create_post.html')

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comment_set.all().order_by('-created_at')
    tags = post.tag_set.all()
    upvotes = post.upvote_set.count()
    is_owner = request.user == post.user if request.user.is_authenticated else False
    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'tags': tags,
        'upvotes': upvotes,
        'is_owner': is_owner
    })

@login_required
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        Comment.objects.create(
            post=post,
            user=request.user,
            content=content
        )
    return redirect('post_detail', post_id=post_id)

@login_required
def upvote_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        Upvote.objects.get_or_create(post=post, user=request.user)
    return redirect('post_detail', post_id=post_id)

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST' and request.user == post.user:
        post.delete()
    return redirect('homepage')

def subseddit(request, subseddit):
    posts = Post.objects.filter(tag__tag=subseddit).order_by('-created_at')[:10]
    return render(request, 'subseddit.html', {'posts': posts, 'subseddit': subseddit})