from django.db import models

# Create your models here.


class Categories(models.TextChoices):
    TECH = 'TC', 'Tecnologia'
    CR = 'CR', 'Curiosidades'
    GR = 'GR', 'Geral'


class Post(models.Model):
    title = models.CharField(max_length=30)
    sub_title = models.CharField(max_length=30)
    content = models.TextField()
    categorias = models.CharField(
        max_length=2,
        choices=Categories.choices,
        default=Categories.GR
    )

    approved = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.title

    