from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
#some fake posts to see how things work.
# Create your views here.
def home(request):
    context = {
      'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html',context)#render is used if we want to pass the whole html page.

# this is what a user will see.We also need to map a url pattern to this view function.
def about(request):
    return render(request, 'blog/about.html',{ 'title':'About'})