from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name= models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name 
    
class Item(models.Model):
    name= models.CharField(max_length=255,unique=True)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True)
    # download_url = models.URLField(default='')
    question_image = models.ImageField(null=True, blank=True)
    correctAnsw = models.CharField(max_length=200, default = 'null')
    file = models.FileField(upload_to='static/file/', max_length=500, null=True, blank=True)
 

    def __str__(self):
        return self.name 


class Point(models.Model):
    x = models.FloatField()
    y = models.FloatField()

    def __str__(self):
        return f"Point ({self.x}, {self.y})"


class Data(models.Model):
   file=models.FileField(upload_to='static/file/',blank=True)