from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, views
from kilonull.models import Post, Category, Tag
from kilonull.serializers import CategorySerializer, PostSerializer


def index(request):
    post_list = Post.objects.filter(hide_listing=False).order_by('published')
    paginator = Paginator(post_list, 5)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'categories': Category.objects.all(),
        'posts': posts,
        'pagination_obj': posts,
    }
    return render(request, 'kilonull/index.html', context)


def view_post(request, slug):
    context = {
        'post': get_object_or_404(Post, slug=slug)
    }
    return render(request, 'kilonull/view_post.html', context)


def view_category(request, slug):
    context = {
        'category': get_object_or_404(Category, slug=slug)
    }
    return render(request, 'kilonull/view_category.html', context)


def view_tag(request, slug):
    context = {
        'tag': get_object_or_404(Tag, slug=slug)
    }
    return render(request, 'kilonull/view_tag.html', context)

###
# API Endpoints
###


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-published")
    serializer_class = PostSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
