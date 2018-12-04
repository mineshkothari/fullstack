# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from .forms import MakePaymentForm, OrderForm
from .models import Order, OrderItem
from courses.models import Module
import stripe

stripe.api_key = settings.STRIPE_SECRET


@login_required(login_url='/account/login/')
def checkout(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)    # NON-EDITABLE FORM (ONLY TO CAPTURE USER DATA)??
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date_ordered = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0

            for module_id in cart.keys():
                module = get_object_or_404(Module, pk=module_id)
                total += module.price
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
        order_form = OrderForm()
        payment_form = MakePaymentForm()

    args = {
        'order_form': order_form,
        'payment_form': payment_form,
        'publishable': settings.STRIPE_PUBLISHABLE,
    }

    return render(request, "checkout/checkout.html", args)
