from django.shortcuts import get_object_or_404
from courses.models import Module


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering every page
    """

    cart = request.session.get('cart', {})

    cart_items = set()
    total = 0

    for module_id in cart.keys():
        module = get_object_or_404(Module, pk=module_id)
        total += module.price
        cart_items.add(module)

    return {'cart_items': cart_items, 'total': total}
