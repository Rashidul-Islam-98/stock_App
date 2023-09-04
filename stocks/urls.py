from django.urls import path
from . import views

urlpatterns = [
    path('', views.stock_list, name='stock_list'),
    path('create-stock/', views.create_stock, name='create_stock'),
    path('edit-stock/<int:stock_id>/', views.edit_stock, name='edit_stock'),
    path('delete-stock/<int:stock_id>/', views.delete_stock, name='delete_stock')
]
