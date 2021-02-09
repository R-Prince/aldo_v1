from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error('There is no items in your bag at the moment')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IJ2sFL7HOKUxpcqiHzLlJitz1nl3fqZTHtuPgUe72Z98YyfPzYixRrXcZCwIc2wO3oDaHYkM1JCjYsnzZbmCWwu00mFFVeHNb',
        'client_secret': 'test client key'
    }

    return render(request, template, context)
