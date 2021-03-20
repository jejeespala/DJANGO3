from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Post


# Create your views here.
def hello_blog(request):
    lista = ['django', 'python', 'git', 'linux', 'ngix']

    list_posts = Post.objects.all()

    data = {'name': 'Curso de Django',
     'lista_tecnologias': lista,
     'posts': list_posts}

    
    return render(request,'index.html', data)
