from django.urls import path
from . import views

urlpatterns = [
    path('initiate/', views.initiate, name='initiate'),
    path('update_status/', views.update_status, name='update_status'),
    path('add_product/', views.add_product, name='add_product'),
    path('show_inventory/', views.show_inventory, name='show_inventory'),
    path('remove_item_from_inventory/', views.remove_item_from_inventory, name='remove_item_from_inventory'),
    path('check_availability/', views.check_availability, name='check_availability'),
]
