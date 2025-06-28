from django.shortcuts import render

# Create your views here.
from .models import Customer

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/customer_list.html', {'customers': customers})