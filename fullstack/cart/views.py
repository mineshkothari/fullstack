# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from django.contrib import messages


def view_cart(request):
    """
    Render the cart
    """
    return render(request, "cart/cart.html")


def add_to_cart(request, module_id):
    """
    Add a Module to cart
    """

    cart = request.session.get('cart', {})
    if module_id not in cart:
        cart[module_id] = module_id

    request.session['cart'] = cart

    return render(request, "cart/cart.html")


def remove_from_cart(request, module_id):
    """
    Delete item from cart
    """
    cart = request.session.get('cart', {})
    if module_id in cart:
        del cart[module_id]
        messages.info(request, "Item has been deleted")

    request.session['cart'] = cart

    return redirect(reverse('view_cart'))
