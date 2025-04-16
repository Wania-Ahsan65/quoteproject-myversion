from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.quote_list_view, name='list'),
    path('create/', views.quote_create_view, name='create'),
    path('<int:pk>/', views.quote_detail_view, name='detail'),
    path('<int:pk>/export/full/', views.export_quote_full, name='export_full'),
    path('<int:pk>/export/sales/', views.export_quote_sales, name='export_sales'),
    path('<int:pk>/export/client-pdf/', views.export_quote_client_pdf, name='export_client_pdf'),

]
