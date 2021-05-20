from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='blog-home'),
    path('about/',views.about,name='blog-about')#this doesnt needed to be added to the project url page it will recoznise it automatically.
]
#First argument of path is '' which signifies home.The empty path maps onto views.home.
