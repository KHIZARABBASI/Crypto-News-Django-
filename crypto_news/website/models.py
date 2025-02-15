from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class NewsSection(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
 

class CreateNews(models.Model):
    title=models.CharField('Title', max_length=200)
    content = CKEditor5Field('Text', config_name='extends')
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='news_category')
    category = models.CharField(max_length=100)
    author = models.CharField('Author', max_length=50),

    def __str__(self):
        return self.title
#----------------------------------------------------------------

class CryptoArticalModel(models.Model):
    title = models.CharField(max_length=100)
    content = CKEditor5Field('Text', config_name='extends')
    image = models.ImageField(upload_to='article_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='news_category')
    category = models.CharField(max_length=100)
    author = models.CharField('Author', max_length=50)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey('website.CryptoArticalModel', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.article}'

