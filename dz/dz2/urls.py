from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.order_list, name='order_list'),
    path('order/create/', views.order_create, name='order_create'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('order/<int:order_id>/update/', views.order_update, name='order_update'),
    path('order/<int:order_id>/delete/', views.order_delete, name='order_delete'),
]