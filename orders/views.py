from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

# Create your views here.


def order_create(request):
    # obtain the current cart from the session
    cart = Cart(request)

    if request.method == "POST":
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            # create a new order in the database
            order = cd.save()
            for item in cart:
                OrderItem.objects.create(product=item['product'], price=item['price'],
                                         quantity=item['quantity'])

            # clear the cart
            cart.clear()
            return render(request, 'orders/order/created.html', {'order': order})

    else:
        form = OrderCreateForm()
        return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})

