from django.shortcuts import render, redirect#to create a registration page.Provided by default from django
from django.contrib import messages
from django.contrib.auth.decorators import login_required#it will display a certain name only when the user is login.
from .form import UserRegisterForm
# Create your views here.
def register(request):
    if request.method == 'POST':#if request is post then validation
        form = UserRegisterForm(request.POST)
        if form.is_valid():#if form is valid we get the username
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created.You are now able to login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'user/register.html',{'form':form})
  
  #we have different types of messages
  #message.debug
  #message.error
  #message.success
  #message.warning
  #message.info
@login_required#decorators add functionality to a existing function.
def profile(request):
    return render(request,'user/profile.html')
