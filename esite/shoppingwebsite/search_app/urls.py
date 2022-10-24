from  django.urls import path#search app2
from . import views

app_name= 'search_app'

urlpatterns =[
    path('',views.SearchResult,name='SearchResult')
]
