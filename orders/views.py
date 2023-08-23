from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
from django.urls import reverse

# Create your views here.


def order_create(request):
    # obtain the current cart from the session
    cart = Cart(request)

    if request.method == "POST":
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            # create a new order in the database
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'], quantity=item['quantity'])
            # clear the cart
            cart.clear()

            # launch asynchronous task: You call the delay() method of the task to execute it asynchronously.
            order_created.delay(order.id)
            # set the order in the session
            request.session['order_id'] = order.id
            # redirect for the payment
            return redirect(reverse('payment:process'))

    else:
        form = OrderCreateForm()
        return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})

