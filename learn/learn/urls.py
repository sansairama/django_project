"""learn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from user import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/',user_views.profile,name='profile'),
    path('register/',user_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='user/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'),name='logout'),
    path('', include('blog.urls')),#if we want to make the blog app the home page just remove the blog/ from path.Keep the path empty.
]
#Any url pattern that we create for any function need to be mentioned here.
#When we use /blog in browser it comes here to see if its present.
#include removes whatever is already used in the path.It removes blog from blog.urls and we now want a empty path in urls page of blog app.
#Remeber that for each app we create we have to create only a single url here.Then we can add more urls in urls.py page of the app without any addition here.
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
