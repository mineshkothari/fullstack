# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from .forms import MakePaymentForm
from .models import Order, OrderItem
from courses.models import Module
import stripe

stripe.api_key = settings.STRIPE_SECRET


@login_required(login_url='/account/login/')
def checkout(request):
    if request.method == 'POST':
        payment_form = MakePaymentForm(request.POST)

        if payment_form.is_valid():

            cart = request.session.get('cart', {})
            total = 0

            for module_id in cart.keys():
                module = get_object_or_404(Module, pk=module_id)
                total += module.price
                order = Order
                order_item = OrderItem(
                    order=order,
                    module=module,
                    )
                order_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="GBP",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, 'Your card was declined')

            if customer.paid:
                messages.success(request, 'You have successfully paid')
                request.session['cart'] = {}
                return redirect(reverse('profile'))
            else:
                messages.error(request, 'Unable to take payment')

        else:
            print(payment_form.errors)
            messages.error(request, 'We were unable to take a payment with that card!')

    else:
        payment_form = MakePaymentForm()

    args = {
        'payment_form': payment_form,
        'publishable': settings.STRIPE_PUBLISHABLE,
    }

    return render(request, "checkout.html", args)