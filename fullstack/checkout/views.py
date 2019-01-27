# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages, auth
from django.template.context_processors import csrf
from .forms import MakePaymentForm
from accounts.forms import UserLoginForm
from .models import Order, OrderItem
from courses.models import Module
import stripe


stripe.api_key = settings.STRIPE_SECRET


@login_required(login_url='/checkout/login/')
def checkout(request):
    if request.method == 'POST':
        payment_form = MakePaymentForm(request.POST)

        if payment_form.is_valid():

            cart = request.session.get('cart', {})
            total = 0

            order = Order(user=request.user)
            order.save()

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

                if customer.paid:
                    order.enrol()
                    order.is_ordered = True
                    order.save()
                    messages.success(request, 'You have successfully paid')
                    request.session['cart'] = {}
                    return redirect(reverse('profile'))

                else:
                    messages.error(request, 'Unable to take payment')

            except stripe.error.CardError:
                messages.error(request, 'Your card was declined')

        else:
            print(payment_form.errors)
            messages.error(request, 'We were unable to take a payment with that card!')

    else:
        payment_form = MakePaymentForm()

    args = {
        'payment_form': payment_form,
        'publishable': settings.STRIPE_PUBLISHABLE,
    }

    return render(request, "checkout/checkout.html", args)


def checkout_login(request):
    if request.user.is_authenticated:
        return redirect(reverse('profile'))
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('checkout'))
            else:
                form.add_error(None, "Your email or password was not recognised")

    else:
        form = UserLoginForm()

    args = {
        'form': form,
        'login_required_message': 'Please login below to proceed to checkout'
    }
    args.update(csrf(request))
    return render(request, 'accounts/login.html', args)
