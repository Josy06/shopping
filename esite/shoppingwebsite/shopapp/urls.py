#This is shopapp urls

from django.urls import path
from shopapp import views
app_name='shopapp'
urlpatterns = [

    path('',views.allproductcat,name='allproductcat'),
    path('<slug:c_slug>/',views.allproductcat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prodcatdetail')#product page2
]
