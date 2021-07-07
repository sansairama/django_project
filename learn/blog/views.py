from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
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
    paginate_by=5
class UserPostListView(ListView):
    model=Post
    template_name='blog/user_posts.html'
    #we can use our own template in class based views as we have used above.
    #<app>/<model>_<viewtype>.html is the default naming convention.
    context_object_name='posts'
    paginate_by=5
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
class PostDetailView(DetailView):
    model=Post
class PostCreateView(LoginRequiredMixin, CreateView):
    model=Post
    fields=['title','content']
    def form_valid(self, form):#current use becomes the author of the post.
        form.instance.author=self.request.user
        return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model=Post
    fields=['title','content']
    def form_valid(self, form):#current use becomes the author of the post.
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):#to make sure that the login user can make changes in his own project
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False  
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post 
    success_url = '/'
    def test_func(self):#to make sure that the login user can delete in his own project
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False     
# this is what a user will see.We also need to map a url pattern to this view function.
def about(request):
    return render(request, 'blog/about.html',{ 'title':'About'})