from decimal import Decimal
from django.conf import settings
# from myshop.shop.models import Product

# import sys, os
# current = os.path.dirname(os.path.realpath(__file__))
# parent = os.path.dirname(current)
# sys.path.append(parent)
# import models
import sys
sys.path.append("C:/Users/user/PycharmProjects/E-commerce_Online_Shop/myshop/shop")  # setting parent path
from shop.models import Product


class Cart(object):
    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        # to make it accessible to other methods of this class
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        # You will build your cart dictionary with product IDs as keys, and for each product key,
        # a dictionary will be a value that includes quantity and price.
        # To guarantee that a product will not be added more than once to the cart.

    def add(self, product, quantity=1, override_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}

        # To update the quantity
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products from the database.
        """
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)

        # You copy the current cart in the cart variable and add the Product instances to it.
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        # convert each item's price back into decimal, and adding a total_price attribute to each item.
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()
