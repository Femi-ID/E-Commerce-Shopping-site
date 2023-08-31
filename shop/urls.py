from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail')
]

# need to translate the URL patterns of the shop application, since they are
# built with variables and do not include any other literals

