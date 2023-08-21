from .cart import Cart

"""A context processor is a Python function that takes the request object as an
argument and returns a dictionary that gets added to the request context.
A context processor to set the current cart into the request context.
With it, you will be able to access the cart in any template.
The cart context processor will be executed every time a template is rendered using Django's RequestContext."""


def cart(request):
    return {'cart': Cart(request)}

# You can read more about RequestContext at https://docs.djangoproject.com/en/3.0/ref/templates/api/#django.template.RequestContext.
# built-in context processors at https://docs.djangoproject.com/en/3.0/ref/templates/api/#built-in-templatecontext-processors.

