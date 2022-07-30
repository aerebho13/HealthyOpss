from django.urls import path
from . import views

app_name= 'store'

urlpatterns=[
    path('rate/<slug:slug>', views.Rate, name='rate'),
    path('test', views.test, name='rate'),
    path('', views.product_all, name='product_all'), #home view with all products
    path('<slug:slug>', views.product_detail, name='product_detail'),#detailed view of all products
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'), #this is the filte by category ex. keto
]
