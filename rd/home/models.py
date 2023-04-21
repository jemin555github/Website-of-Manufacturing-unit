from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=50, default='Bottel')
    price=models.CharField(max_length=50, default='plastil')
    type=models.CharField(max_length=50, default='sport')    
    image = models.ImageField(upload_to='category_images', default='default_image.jpg')
     
    def __str__(self):
        return self.name
    

class Slider(models.Model):
    image= models.ImageField(upload_to='category_images', default='default_image.jpg')