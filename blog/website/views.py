from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_blog(request):
    lista = ['django', 'python', 'git', 'linux', 'ngix']
    data = {'name': 'Curso de Django', 'lista_tecnologias': lista}
    return render(request,'index.html', data)
