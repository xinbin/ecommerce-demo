from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Category, Product


def home(request):
    return render(request, "ecommerce/home.html")


def catalog(request):
    items = Product.objects.filter(featured=True, status=Product.ACTIVE)

    return render(request, "ecommerce/index.html", {
        'products': items,
        'carousel': True
    })


def products(request, cid):
    try:
        category = Category.objects.get(id=cid)
    except Category.DoesNotExist:
        return render(request, "ecommerce/not-found.html", {"message": "Category not found"}, status=404)
    items = category.product_set.filter(status=Product.ACTIVE)
    return render(request, "ecommerce/index.html", {
        'products': items,
        'title': category.name
    })


def product(request, pid):
    try:
        item = Product.objects.get(id=pid)
    except Product.DoesNotExist:
        return render(request, "ecommerce/not-found.html", {"message": "Product not found"}, status=404)
    return render(request, "ecommerce/product.html", {'product': item})


def specials(request):
    # Cookie based page
    if 'PRODUCT' not in request.COOKIES:
        items = Product.objects.filter(special=True, status=Product.ACTIVE)
        return render(request, "ecommerce/index.html", {
            'products': items,
            'title': 'All Specials',
            'specials': True
        })

    cid = request.COOKIES['PRODUCT']
    try:
        category = Category.objects.get(id=cid)
    except Category.DoesNotExist:
        message = "Invalid cookie"
        return render(request, "ecommerce/not-found.html", {'message': message})
    items = category.product_set.filter(special=True, status=Product.ACTIVE)
    return render(request, "ecommerce/index.html", {
        'products': items,
        'specials': True,
        'title': '%s Specials' % category.name
    })


def cart_display(request):
    items = []
    cart = request.session['cart']
    cart['subtotal'] = 0
    if 'items' in cart:
        for pid, value in cart['items'].iteritems():
            try:
                product = Product.objects.get(id=pid)
                product.qty = value['qty']
                product.total = value['qty'] * float(product.price)
                cart['subtotal'] += product.total
                items.append(product)
            except Product.DoesNotExist:
                pass

    return render(request, "ecommerce/cart.html", {'cart': cart, 'items': items})


def cart_add(request, pid):
    cart = request.session['cart']
    if 'items' not in cart:
        cart['items'] = dict()
    item = cart['items'].get(pid, dict({'qty': 0}))
    item['qty'] += 1
    cart['items'][pid] = item
    request.session['cart'] = cart
    return HttpResponseRedirect('/cart')


def cart_remove(request, pid):
    cart = request.session['cart']
    try:
        del(cart['items'][pid])
    except IndexError:
        pass
    request.session['cart'] = cart
    return HttpResponseRedirect('/cart')
