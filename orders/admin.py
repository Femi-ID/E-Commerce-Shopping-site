from django.contrib import admin
from .models import Order, OrderItem
import csv
import datetime
from django.http import HttpResponse
from django.urls import reverse
from django.utils.safestring import mark_safe
# Register your models here.

"""An inline allows you to include a model on the same edit page as its related model."""


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


def export_to_csv(modeladmin, request, queryset):
    """to create a custom administration action to download a list of orders as a CSV file"""
    opts = modeladmin.model._meta
    content_disposition = f'attachment; filename={opts.verbose_name}.csv'
    # To create an instance of HttpResponse, specifying the text/csv content type,
    # to tell the browser that the response has to be treated as a CSV file
    response = HttpResponse(content_type='text/csv')
    # to indicate that the HTTP response contains an attached file.
    response['Content-Disposition'] = content_disposition
    # a CSV writer object that will write to the 'response' object
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not
              field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows: iterate over the given QuerySet and write a row for each object returned by the QuerySet
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response


# learn more about generating CSV files with Django at: https://docs.djangoproject.com/en/3.0/howto/outputting-csv/
# customize the display name for the action in the actions dropdown element of the admin site using 'short_description'
export_to_csv.short_description = 'Export to CSV'


def order_detail(obj):
    url = reverse('orders:admin_order_detail', args=[obj.id])
    return mark_safe(f'<a href="{url}">View</a>')


def order_pdf(obj):
    url = reverse('orders:admin_order_pdf', args=[obj.id])
    return mark_safe(f'<a href="{url}">PDF</a>')


order_pdf.short_description = 'Invoice'
# If you specify a short_description attribute for your callable, Django will use it for the name of the column.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'postal_code',
                    'city', 'paid', 'created', 'updated', order_detail, order_pdf]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    actions = [export_to_csv]


# Avoid using mark_safe on input that has come from the user to avoid cross-site scripting (XSS).
