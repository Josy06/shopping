from django.urls import path #cartpart2
from . import views

app_name='cart'

urlpatterns = [
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),# cart 8 video
    path('',views.cart_details,name='cart_detail'),#cartpart2
    path('remove/<int:product_id>/',views.cart_remove,name='cart_remove'),#items Deletion
    path('full_remove/<int:product_id>/',views.full_remove,name='full_remove')
]