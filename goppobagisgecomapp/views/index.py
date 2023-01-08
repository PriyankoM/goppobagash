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
    if bookdetailspage:
        mybookdata={}
        bookroducts=Products.get_products_by_id(bookdetailspage)
        mybookdata["mybookdata"]=bookroducts[0]
        print(bookroducts[0])
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





