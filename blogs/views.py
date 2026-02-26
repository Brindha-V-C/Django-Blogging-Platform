from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, Category
from django.db.models import Q

def post_by_category(request, category_id):

    #Fetch posts that belongs to the category_id 
    posts = Blog.objects.filter(status = "Published", category = category_id)

    #To show custom action when the category does not exists
    try:
        category_name = Category.objects.get(pk=category_id)
    except:
        #Redirect to home page when category does not exist
        return redirect('home')
    
    context = {
        'posts': posts,
        'category_name': category_name
    }

    return render(request, 'post_by_category.html', context)


def single_blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug, status="Published")

    context = {
        'blog': blog
    }

    return render(request, 'single_blog.html', context)

def search(request):
    keyword = request.GET.get('keyword')

    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_content__icontains=keyword), status="Published")

    context = {
        "blogs": blogs,
        "keyword": keyword
    }

    return render(request, 'search.html', context)