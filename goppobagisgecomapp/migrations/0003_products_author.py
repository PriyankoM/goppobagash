# Generated by Django 4.1.3 on 2023-01-03 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goppobagisgecomapp', '0002_category_products_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='author',
            field=models.CharField(default='no Author', max_length=100),
        ),
    ]