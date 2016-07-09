from django.shortcuts import render
from models import Article, Category
from django.shortcuts import redirect

# Create your views here.


def posts_list(request):
    context = {
        'news': Article.objects.all().order_by('-created_at'),
        'categories': Category.objects.all()
    }
    return render(request, 'posts/posts_list.html', context)


def post_detail(request, post_id):
    post = Article.objects.get(id=post_id)
    context = {
        'post': post,
        'categories': Category.objects.all(),
    }
    return render(request, 'posts/post_detail.html', context)


def by_category_list(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    context = {
        'post': category.article_set.all(),
        'categories': Category.objects.all(),
    }
    return render(request, 'posts/posts_list.html', context)


def likes(request, post_id):
    post = Article.objects.get(id=post_id)
    post.likes += 1
    post.save()
    return redirect('/index')


def dislikes(request, post_id):
    post = Article.objects.get(id=post_id)
    post.dislikes += 1
    post.save()
    return redirect('/index')
