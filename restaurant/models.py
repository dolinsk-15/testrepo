from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)  # Заголовок статьи
    author = models.CharField(max_length=100)  # Автор статьи
    content = models.TextField()  # Содержание статьи
    published_date = models.DateField(auto_now_add=True)  # Дата публикации статьи

    def __str__(self):
        return self.title
    
    
    
class just(models.Model):
    title = models.CharField(max_length=100)  # Заголовок статьи
    author = models.CharField(max_length=100)  # Автор статьи
    content = models.TextField()  # Содержание статьи
    published_date = models.DateField(auto_now_add=True)  # Дата публикации статьи

    def __str__(self):
        return self.title