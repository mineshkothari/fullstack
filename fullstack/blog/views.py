# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from django.template.context_processors import csrf
from .models import Post
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required


def post_list(request):
    """
    Render blog posts on the page and order them by descending published date
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-published_date')
    return render(request, 'blog/blogposts.html', {'posts': posts})


def post_detail(request, post_id):
    """
    Render individual blog post articles
    """
    post = get_object_or_404(Post, pk=post_id)
    post.views += 1
    post.save()
    return render(request, 'blog/postdetail.html', {'post': post})


def top_posts(request):
    """
    Render the published blog posts in order of popularity and limit to 5 posts
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-views')[:5]
    return render(request, 'blog/blogposts.html', {'posts': posts})


@login_required(login_url='/account/login/')
def new_blog_post(request):
    """
    Submit or render new blog post form
    """
    # First check if user is staff. If True and method is POST then save blog
    if request.user.is_staff:
        if request.method == 'POST':
            form = BlogPostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect(post_detail, post.pk)

        # If method is GET, render blank from
        else:
            form = BlogPostForm()

        args = {
            'form': form,
            'form_title': 'Add New Blog'
        }

        args.update(csrf(request))

        return render(request, 'blog/blogpostform.html', args)

    # If user does not have Staff status, redirect to blog homepage
    else:
        return redirect(reverse('blog'))


@login_required(login_url='/account/login/')
def edit_post(request, post_id):
    """
    Submit or render edit blog post form
    """
    post = get_object_or_404(Post, pk=post_id)

    # First check if user is staff. If True and method is POST then update blog
    if request.user.is_staff:
        if request.method == "POST":
            form = BlogPostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect(post_detail, post.pk)

        # If method is GET, render blank from
        else:
            form = BlogPostForm(instance=post)

        args = {
            'form': form,
            'form_title': 'Edit ' + post.title
        }

        return render(request, 'blog/blogpostform.html', args)

    # If user does not have Staff status, redirect to blog homepage
    else:
        return redirect(reverse('blog'))
