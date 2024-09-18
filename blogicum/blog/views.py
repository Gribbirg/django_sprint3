from django.http import Http404
from django.shortcuts import render


def index(request):
    template_name = 'blog/index.html'
    rev_posts = posts[::-1]
    context = {
        'posts': rev_posts,
    }
    return render(request, template_name, context)


def post_detail(request, id):
    posts_with_id = [post for post in posts if post['id'] == id]
    if len(posts_with_id) == 0:
        raise Http404
    post = posts_with_id[0]

    template_name = 'blog/detail.html'
    context = {
        'post': post,
    }
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    context = {
        'category': {
            'slug': category_slug,
        }
    }
    return render(request, template_name, context)
