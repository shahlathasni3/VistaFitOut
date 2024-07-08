from django.db import models
from Category.models import Category

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug         = models.SlugField(max_length=200, unique=True)
    images       = models.ImageField(upload_to='photos/products')
    category     = models.ForeignKey(Category,on_delete=models.CASCADE)



    def __str__(self):
        return self.product_name
    


