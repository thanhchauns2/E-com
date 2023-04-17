from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register_product/', views.register_product, name='register_product'),
    path('inititate_inventory/', views.inititate_inventory, name='inititate_inventory'),
    path('add_product_to_inventory/', views.add_product_to_inventory, name='add_product_to_inventory'),
    path('remove_product_from_inventory/', views.remove_product_from_inventory, name='remove_product_from_inventory'),
    path('show_inventory/', views.show_inventory, name='show_inventory'),
    path('add_product_to_cart/', views.add_product_to_cart, name='add_product_to_cart'),
    path('remove_item_from_cart/', views.remove_item_from_cart, name='remove_item_from_cart'),
    path('show_cart/', views.show_cart, name='show_cart'),
    path('purchase/', views.purchase, name='purchase'),
    path('track_order/', views.track_order, name='track_order'),
    path('update_order/', views.update_order, name='update_order'),
]
