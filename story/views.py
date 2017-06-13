# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.utils import timezone
from story.models import Post
from story.forms import PostForm


def home(request):
    return render(request, 'base.html')


def story(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog_homepage.html', context)


def specific(request, blog_id):
    context = {
        'post': Post.objects.get(id=blog_id)
    }
    return render(request, 'specific_blogpage.html', context)


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            context = {
                'posts': Post.objects.all()
            }
            return render(request, 'blog_homepage.html', context)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})
