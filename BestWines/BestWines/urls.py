from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from accounts import views

urlpatterns = [
    path('', lambda request: redirect('login')),  # 👈 this handles the empty path
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('quotes/', include('quotes.urls')),
    path('customers/', include('customers.urls')),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]

