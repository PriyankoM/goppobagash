from django.db import models
from .products import Products
from .customer import Customer
import datetime


class Orders(models.Model):
    product = models.ForeignKey(Products,
                                on_delete=models.CASCADE)
    # customer = models.ForeignKey(Customer,
    #                              on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    Name=models.CharField (max_length=100, default='', blank=False)
    Email=models.EmailField(blank=False,default='')
    PostOffice=models.CharField(max_length=200,default='',blank=False)
    CityOrVillage=models.CharField(max_length=200,default='',blank=False)
    PinCode=models.CharField(max_length=50,default='',blank=False)
    State=models.CharField(max_length=50,default='',blank=False)
    address = models.CharField (max_length=100, default='', blank=True)
    phone = models.CharField (max_length=50, default='', blank=True)
    date = models.DateField (default=datetime.datetime.today)
    status = models.BooleanField (default=False)
    paymentId=models.CharField(max_length=400,default="",blank=False)
    orderId=models.CharField(max_length=400,default="",blank=False)
    SignatureId=models.CharField(max_length=600,default="",blank=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Orders.objects.filter(customer=customer_id).order_by('-date')

