from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','sub_title','content','categorias','approved']
    search_fields = ['title','sub_title','content']

    def get_queryset(self, request):
        return Post.objects.filter(approved=True)

admin.site.register(Post, PostAdmin)
