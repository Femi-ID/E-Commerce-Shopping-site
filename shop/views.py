from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm


# Create your views here.


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        language = request.LANGUAGE_CODE
        category = get_object_or_404(Category, translations__language_code=language,
                                     translations__slug=category_slug)
        # to get the requested category through slug
        products = products.filter(category=category)
        # To display lists of products under a particular category

    return render(request, 'shop/product/list.html', {'category': category,
                                                      'categories': categories,
                                                      'products': products})


def product_detail(request, id, slug):
    language = request.LANGUAGE_CODE
    product = get_object_or_404(Product, id=id, translations__language_code=language,
                                translations__slug=slug, available=True)
    # You could've retrieved a product instance with only ID,
    # but you include slug in the URL to build SEO-friendly URLs for products.

    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})
