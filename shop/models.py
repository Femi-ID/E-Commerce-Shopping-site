from django.db import models
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields
"""django-parler manages translations by generating another model for each translatable model"""
# Create your models here.


class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=200, db_index=True),
        slug = models.SlugField(max_length=200, unique=True)
    )

    class Meta:
        # ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=200, db_index=True),
        slug = models.SlugField(max_length=200, db_index=True),
        description=models.TextField(blank=True)
    )
    # There is a one-to-many relationship from 'Product' to 'ProductTranslation'.
    # A 'ProductTranslation' object will exist for each available language of each Product object
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # slug: The slug for this product to build beautiful URLs.
    # price: instead of FloatField to avoid rounding issues
    # available: to enable/disable the product in the catalog.

    # class Meta:
    #     ordering = ('name',)
    #     index_together = (('id', 'slug'),)  # to specify an index for the id and slug fields together
    # read more about the django-parler module's compatibility with Django
    # at https://django-parler.readthedocs.io/en/latest/compatibility.html.
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
    # convention to retrieve the URL for a given object, using the pattern defined in urls.py
