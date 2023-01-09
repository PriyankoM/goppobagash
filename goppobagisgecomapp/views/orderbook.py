from django.views import View
from django.shortcuts import render , redirect , HttpResponseRedirect
from goppobagisgecomapp.models.orders import Orders
from goppobagisgecomapp.models.products import Products

class OrderBook(View):
    mybookData=None
    def get(self,request):
        bookid=request.GET.get('orderbook')
        data={}
        if bookid:
            bookData=Products.get_products_by_id(bookid)
            data['bookData']=bookData[0]
            if bookData:
                return render(request, 'address.html', data)
            else:
                return HttpResponseRedirect(f'/ourbooks')
        else:
            return HttpResponseRedirect(f'/ourbooks')

    def post(self , request):
        print('rrrr')
        print(self.mybookData)
        print(request.POST)
        if(request.POST.get('bookid') and request.POST.get('firstname') and request.POST.get('email') and request.POST.get('address') and request.POST.get('city/Vill') and request.POST.get('P.O.') and request.POST.get('state') and request.POST.get('Pin') and request.POST.get('phoneNumber') ):
            prodect=Products.get_products_by_id(request.POST.get('bookid'))
            
            order=Orders(product=Products(id=request.POST.get('bookid')),price=prodect[0].get('price'),Name=request.POST.get('firstname'),Email=request.POST.get('email'), PostOffice=request.POST.get('P.O.'),CityOrVillage=request.POST.get('city/Vill'),PinCode=request.POST.get('Pin'),State=request.POST.get('state'),address=request.POST.get('address'),phone=request.POST.get('phoneNumber'))

            order.save()
        return HttpResponseRedirect(f'/ourbooks')
