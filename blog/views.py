from django.shortcuts import render
from django.core.paginator import Paginator

from blog.models import Post, Popular, Category, Banner


def home(request):
  # posts = Post.objects.all()
  populares = Popular.objects.all()
  categories = Category.objects.all()
  banners = Banner.objects.all()

  paginator = Paginator(Post.objects.all(), 2)
  page = request.GET.get('page')
  posts = paginator.get_page(page)
  nums = 'a' * posts.paginator.num_pages
  nextpage1 = posts.number
  nextpage2 = nextpage1 + 1
  nextpage3 = nextpage2 + 1
  nextpage4 = nextpage3 + 1

  context = {
    'posts': posts,
    'populares': populares,
    'categories': categories,
    'banners': banners,
    'page': 'Últimas notícias',
    'nums': nums,
    'nextpage1': nextpage1,
    'nextpage2': nextpage2,
    'nextpage3': nextpage3,
    'nextpage4': nextpage4,
  }
  return render(request, 'home.html', context)


def homeSearch(request):
  if request.method == 'POST':
    searched = request.POST.get('searched')
    paginator = Paginator(Post.objects.filter(title__contains=searched), 2)
  else:
    paginator = Paginator(Post.objects.all(), 2)

  populares = Popular.objects.all()
  categories = Category.objects.all()
  banners = Banner.objects.all()

  page = request.GET.get('page')
  posts = paginator.get_page(page)
  nums = 'a' * posts.paginator.num_pages
  nextpage1 = posts.number
  nextpage2 = nextpage1 + 1
  nextpage3 = nextpage2 + 1
  nextpage4 = nextpage3 + 1

  context = {
    'posts': posts,
    'populares': populares,
    'categories': categories,
    'banners': banners,
    'page': 'Últimas notícias',
    'nums': nums,
    'nextpage1': nextpage1,
    'nextpage2': nextpage2,
    'nextpage3': nextpage3,
    'nextpage4': nextpage4,
  }
  return render(request, 'home.html', context)


def homeCategory(request, category_id):
  populares = Popular.objects.all()
  categories = Category.objects.all()
  banners = Banner.objects.all()
  categorieName = Category.objects.get(pk=category_id)

  paginator = Paginator(Post.objects.filter(category_id=category_id), 1)
  page = request.GET.get('page')
  posts = paginator.get_page(page)
  nums = 'a' * posts.paginator.num_pages
  nextpage1 = posts.start_index()
  nextpage2 = posts.start_index() + 1
  nextpage3 = posts.start_index() + 2
  nextpage4 = posts.start_index() + 3

  context = {
    'posts': posts,
    'populares': populares,
    'categories': categories,
    'banners': banners,
    'page': categorieName,
    'nums': nums,
    'nextpage1': nextpage1,
    'nextpage2': nextpage2,
    'nextpage3': nextpage3,
    'nextpage4': nextpage4,
  }
  return render(request, 'home.html', context)


def post(request, post_id):
  post = Post.objects.get(pk=post_id)
  populares = Popular.objects.all()

  context = {
    'post': post,
    'populares': populares
  }
  return render(request, 'post.html', context)
