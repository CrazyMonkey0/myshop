from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from coupons.forms import CouponApplyForm
from shop.recommender import Recommender
from .cart import Cart
from .forms import CartAddProductForm


def cart_detail(request):
    """
    View displaying products from the shopping cart
    """
    cart = Cart(request)
    #
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'],
                     'override': True}
        )
    coupon_apply_form = CouponApplyForm()
    r = Recommender()
    cart_products = [item['product'] for item in cart]
    recommended_products = r.products_bought(
        [item['product'] for item in cart])
    recommended_products = r.suggest_products_for(cart_products,
                                                  max_results=4)
    return render(request, 'cart/detail.html',
                  {'cart': cart, 'coupon_apply_form': coupon_apply_form,
                   'recommended_products': recommended_products})


@require_POST
def cart_add(request, product_id):
    """
    View used to add products to shopping cart or update quantity products
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],
                 update_quantity=cd['override'])
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, product_id):
    """
    View removing products from the cart
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')
