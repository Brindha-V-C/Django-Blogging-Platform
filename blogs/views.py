from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Blog, Category

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