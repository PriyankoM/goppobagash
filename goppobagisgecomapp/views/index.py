from django.shortcuts import render , redirect , HttpResponseRedirect
from goppobagisgecomapp.models.products import Products
from goppobagisgecomapp.models.category import Category
from django.views import View


class Index(View):
    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('homepage')


    def get(self , request):
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')



def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    bookdetailspage=request.GET.get('bookdetails')

    if request.GET.get('orderbook'):
        a=request.GET.get('orderbook')
        return HttpResponseRedirect(f'/orderbook?orderbook={a}')

    if bookdetailspage:
        mybookdata={}
        bookroducts=Products.get_products_by_id(bookdetailspage)
        mybookdata["mybookdata"]=bookroducts[0]
        orginalPrice = bookroducts[0]['price']
        discountPercentage = bookroducts[0]['Discount']
        print(bookroducts[0]['Discount'])
        totalAmount = round(orginalPrice-((discountPercentage/100)*orginalPrice), 2)
        mybookdata['totalAmount']=totalAmount+bookroducts[0]['DeliveryCharge']
        mybookdata['discountPrice']=totalAmount
        # productCatagory=
        return render(request, 'books-detail.html', mybookdata)
    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    else:
        products = Products.get_all_products()

    data = {}
    data['products'] = products
    data['categories'] = categories
    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)


def ourbooks(request):
    data={}
    products = Products.get_all_products()
    data['products'] = products
    print(data['products'])
    return render(request, "books.html",data)





