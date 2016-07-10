from django.shortcuts import render
from models import Posts, Categories, Comments
from django.shortcuts import redirect

# Create your views here.


def posts_list(request):
    context = {
        'news': Posts.objects.all().order_by('-created_at'),
        'categories': Categories.objects.all()
    }
    return render(request, 'posts/posts_list.html', context)


def post_detail(request, post_id):
    post = Posts.objects.get(id=post_id)
    comments = Comments.objects.filter(post=post_id)
    context = {
        'post': post,
        'categories': Categories.objects.all(),
        'comments': comments,
    }
    return render(request, 'posts/post_detail.html', context)


def by_category_list(request, category_slug):
    category = Categories.objects.get(slug=category_slug)
    context = {
        'post': category.posts_set.all(),
        'categories': Categories.objects.all(),
    }
    return render(request, 'posts/posts_list.html', context)


def likes(request, post_id):
    post = Posts.objects.get(id=post_id)
    post.likes += 1
    post.save()
    return redirect('/index')


def dislikes(request, post_id):
    post = Posts.objects.get(id=post_id)
    post.dislikes += 1
    post.save()
    return redirect('/index')


def by_likes_down(request):
    posts = Posts.objects.all().order_by('likes')
    context = {
        'news': posts,
        'categories': Categories.objects.all()
    }
    return render(request, 'posts/posts_like.html', context)


def by_likes_up(request):
    posts = Posts.objects.all().order_by('-likes')
    context = {
        'news': posts,
        'categories': Categories.objects.all(),
    }
    return render(request, 'posts/posts_like.html', context)


def by_dislikes_down(request):
    posts = Posts.objects.all().order_by('dislikes')
    context = {
        'news': posts,
        'categories': Categories.objects.all()
    }
    return render(request, 'posts/posts_like.html', context)


def by_dislikes_up(request):
    posts = Posts.objects.all().order_by('-dislikes')
    context = {
        'news': posts,
        'categories': Categories.objects.all(),
    }
    return render(request, 'posts/posts_like.html', context)
