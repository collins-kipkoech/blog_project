from django.shortcuts import render

posts = [
    {
        'title':'new post',
        'author':'collins',
        'content':'new post content',
    },
    {
        'title':'new post 1',
        'author':'collins',
        'content':'new post content two',
    }
]
# Create your views here.
def home_view(request):
    context = {'posts':posts}
    return render(request,'blog/home.html',context)
   
