from django.views import View
from django.shortcuts import render, redirect, HttpResponseRedirect
from goppobagisgecomapp.models.orders import Orders
from goppobagisgecomapp.models.products import Products
import razorpay


class OrderBook(View):
    mybookData = None
    client = razorpay.Client(
        auth=("rzp_test_begQBGyjyI3ha1", "g7kTdiKptYQmb4bqZiFnQEj4"))

    def get(self, request):
        bookid = request.GET.get('orderbook')
        data = {}

        if bookid:
            bookData = Products.get_products_by_id(bookid)
            orginalPrice = bookData[0]['price']
            discountPercentage = bookData[0]['Discount']
            
            totalAmount = round(
                orginalPrice-(discountPercentage/100)*orginalPrice, 2)
            print(totalAmount)
            data['bookData'] = bookData[0]
            totalAmountPaisa=(totalAmount+bookData[0]['DeliveryCharge'])*100
            data['totalAmountPaisa']=totalAmountPaisa

            if bookData:
                self.client.order.create({
                    "amount": totalAmountPaisa,
                    "currency": "INR",
                    "receipt": "receipt#1",
                    "notes": {
                        "key1": "value3",
                        "key2": "value2"
                    }
                })
                return render(request, 'address.html', data)
            else:
                return HttpResponseRedirect(f'/ourbooks')
        else:
            return HttpResponseRedirect(f'/ourbooks')

    def post(self, request):
        print('rrrr')
        print(self.mybookData)
        print(request.POST)
        if (request.POST.get('bookid') and request.POST.get('firstname') and request.POST.get('email') and request.POST.get('address') and request.POST.get('city/Vill') and request.POST.get('P.O.') and request.POST.get('state') and request.POST.get('Pin') and request.POST.get('phoneNumber')):
            prodect = Products.get_products_by_id(request.POST.get('bookid'))

            order = Orders(product=Products(id=request.POST.get('bookid')), price=prodect[0].get('price'), Name=request.POST.get('firstname'), Email=request.POST.get('email'), PostOffice=request.POST.get(
                'P.O.'), CityOrVillage=request.POST.get('city/Vill'), PinCode=request.POST.get('Pin'), State=request.POST.get('state'), address=request.POST.get('address'), phone=request.POST.get('phoneNumber'))

            order.save()
        return HttpResponseRedirect(f'/ourbooks')


# def PaymentSuccess(request):
