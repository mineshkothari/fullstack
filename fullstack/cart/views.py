# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse


def view_cart(request):
    """
    Render the cart
    """
    return render(request, "cart/cart.html")


def add_to_cart(request, id):
    """
    Add a Module to cart
    """

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id)

    request.session['cart'] = cart
    return redirect(reverse('courses'))
