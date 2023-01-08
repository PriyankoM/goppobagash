from django.db import models

class Category(models.Model):
    name= models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
    @staticmethod
    def get_category_by_id(ids):
        Category.objects.filter(id__in=ids).values()

    def __str__(self):
        return self.name
