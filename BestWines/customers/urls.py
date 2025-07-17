from django.urls import path
from . import views
from .views import customer_autocomplete

app_name = 'customers'

urlpatterns = [
    path('', views.customer_list, name='list'),
    path('create/', views.create_customer, name='create'),
    path('update/<int:pk>/', views.update_customer, name='update'),
    path('delete/<int:pk>/', views.delete_customer, name='delete'),
    path('autocomplete/', customer_autocomplete, name='customer_autocomplete'),
]

