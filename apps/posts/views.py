from django.shortcuts import render
from django.http import Http404
from models import Posts, Categories, Comments
from django.shortcuts import redirect
from forms import PostsForm
from django.contrib.auth.decorators import login_required

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
    try:
        category = Categories.objects.get(slug=category_slug)
    except Categories.DoesNotExist:
        raise Http404
    context = {
        'news': category.posts_set.all(),
        'categories': Categories.objects.all()
    }
    return render(request, 'posts/posts_list.html', context)


@login_required(login_url='/error/')
def likes(request, post_id):
    post = Posts.objects.get(id=post_id)
    post.likes += 1
    post.save()
    return redirect('/index')


@login_required(login_url='/error/')
def dislikes(request, post_id):
    post = Posts.objects.get(id=post_id)
    post.dislikes += 1
    post.save()
    return redirect('/index')


def by_likes_filter(request, filter_by):
    if filter_by == 'lup':
        posts = Posts.objects.all().order_by('-likes')
    elif filter_by == 'ldown':
        posts = Posts.objects.all().order_by('likes')
    elif filter_by == 'dup':
        posts = Posts.objects.all().order_by('-dislikes')
    elif filter_by == 'ddown':
        posts = Posts.objects.all().order_by('dislikes')
    context = {
        'news': posts,
        'categories': Categories.objects.all()
    }
    return render(request, 'posts/posts_like.html', context)


@login_required(login_url='/error/')
def create_post(request):
    if request.user.is_staff:
        form = PostsForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('/index')
        return render(request, 'posts/create_post.html', {'form': form})
    return redirect('/error/')


@login_required(login_url='/error/')
def create_category(request):
    if request.user.is_staff:
        if 'category_title' in request.GET and 'category_slug' in request.GET:
            Categories.objects.create(
                title=request.GET['category_title'],
                slug=request.GET['category_slug']
            )
        return render(request, 'posts/create_category.html', {})
    return redirect('/error/')


@login_required(login_url='/error/')
def edit_post(request, post_id):
    if request.user.is_staff:
        post = Posts.objects.get(id=post_id)
        form = PostsForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/index')
        return render(request, 'posts/create_post.html', {'form': form})
    return redirect('/error/')


@login_required(login_url='/error/')
def delete_post(request, post_id):
    if request.user.is_staff:
        post = Posts.objects.get(id=post_id)
        post.delete()
        return redirect('/index')
    return redirect('/error/')


def search_post(request):
    posts = Posts.objects.filter(icontains=request.GET.get('q'))
    context = {
        'news': posts,
        'categories': Categories.objects.all()
    }
    return render(request, 'posts/posts_list.html', context)
