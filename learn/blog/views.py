from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post
#some fake posts to see how things work.
# Create your views here.
def home(request):
    context = {
      'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html',context)
    #render is used if we want to pass the whole html page.

class PostListView(ListView):
    model=Post
    template_name='blog/home.html'
    #we can use our own template in class based views as we have used above.
    #<app>/<model>_<viewtype>.html is the default naming convention.
    context_object_name='posts'
    ordering=['-date_posted']
class PostDetailView(DetailView):
    model=Post
# this is what a user will see.We also need to map a url pattern to this view function.
def about(request):
    return render(request, 'blog/about.html',{ 'title':'About'})