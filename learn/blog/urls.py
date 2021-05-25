from django.urls import path
from .views import PostListView,PostDetailView
from . import views
urlpatterns = [
    path('',PostListView.as_view(),name='blog-home'),
     path('posts/<int:pk>',PostDetailView.as_view(),name='post_detail'), 
     #the pk value helps us to go to the post that we want to(primary key)
    path('about/',views.about,name='blog-about')#this doesnt needed to be added to the project url page it will recoznise it automatically.
]
#First argument of path is '' which signifies home.The empty path maps onto views.home.
