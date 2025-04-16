from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('upload/', views.product_upload_view, name='upload'),
    path('', views.product_list_view, name='list'),
    path('edit/<str:product_code>/', views.product_edit_view, name='edit'),
]
