from django.db import models
from .category import Category
from django.core.paginator import Paginator
class Products(models.Model):
    author=models.CharField(max_length=100,default="no Author")
    name = models.CharField(max_length=60)
    price= models.FloatField(default=0.0)
    Discount=models.FloatField(default=0.0,verbose_name="Discount Percentage")
    category= models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description= models.CharField(max_length=250, default='', blank=True, null= True)
    image= models.ImageField(upload_to='uploads/products/')
    DeliveryCharge=models.IntegerField(default=10,blank=True)

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids).values()

    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter (category=category_id)
        else:
            return Products.get_all_products()