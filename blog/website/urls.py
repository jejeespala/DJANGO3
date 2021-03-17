from django.urls.conf import path,include
from .views import hello_blog

urlpatterns = [
    path('', hello_blog),
    

]
