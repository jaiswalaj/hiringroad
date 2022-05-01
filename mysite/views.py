from django.http import HttpResponse
from django.shortcuts import render
from mysite.models import Post, Category

def testpage(request):
    # Load posts from DB
    posts = Post.objects.all()[:11]
    data = {
      'posts' : posts
    }
    return render(request, 'testpage.html', data)

def index(request):
    # Load posts from DB
    posts = Post.objects.filter().order_by('add_date').reverse()[:10]  
    data = {
      'posts' : posts
    }
    return render(request, 'index.html', data)

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

def privacypolicy(request):
    return render(request, 'privacypolicy.html')

def jobcategories(request):
    return render(request, 'jobcategories.html')

def jobcategorypost(request, url):
    category = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=category)
    return render(request, 'jobposts.html', {'category' : category, 'posts' : posts})

def singlejobpost(request, url):
    post = Post.objects.get(url=url)
    return render(request, 'singlejobpost.html', {'post' : post})