from django.shortcuts import render, redirect, get_object_or_404
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
from .models import Order
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint

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


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/detail.html', {'order': order})


@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/order/pdf.html', {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    # use WeasyPrint to generate a PDF file from the rendered HTML code and write the file to the HttpResponse object
    weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])
    # Then use the static file css/pdf.css to add CSS styles to the generated PDF file.
    return response

# 'response': generates a new HttpResponse object specifying the application/pdf content type and
# including the Content-Disposition header to specify the filename.

