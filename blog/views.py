from django.shortcuts import render,redirect
from .models import Post
from .forms import RegisterForm
from django.contrib import messages


# Create your views here.
def home_view(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request,'blog/home.html',context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your account has been created successfully')
            return redirect('home-view')
    else:
        form = RegisterForm()
       
    context = {
        'form':form,
    }
    return render(request,'blog/register.html',context)
   
