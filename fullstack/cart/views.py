# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from courses.models import Module


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
    if module_id not in cart.keys():
        cart[module_id] = module_id

    request.session['cart'] = cart

    return render(request, "cart/cart.html")
