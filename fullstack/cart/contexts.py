from django.shortcuts import get_object_or_404
from courses.models import Module


def cart_contents(request):
    """
    Ensure cart contents are available when rendering each page
    """

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    for module_id in cart.items():
        module = get_object_or_404(Module, pk=module_id)
        total += module.price
        cart_items.append({'module_id': module_id, 'module': module})

    return {'cart_items': cart_items, 'total': total}
