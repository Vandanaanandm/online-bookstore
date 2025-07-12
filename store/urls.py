from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),


    path('books/', views.book_list),
    path('bookdetails/', views.book_detail),

    
    path('orders/', views.order_list),
]
