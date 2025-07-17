from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm
from django.http import JsonResponse

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/customer_list.html', {'customers': customers})

def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers:list')
    else:
        form = CustomerForm()
    return render(request, 'customers/create_customer.html', {'form': form})

def update_customer(request, pk):
    customer = Customer.objects.get(pk=pk)
    form = CustomerForm(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('customers:list')
    return render(request, 'customers/update_customer.html', {'form': form})


def delete_customer(request, pk):
    customer = Customer.objects.get(pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customers:list')
    return render(request, 'customers/delete_customer.html', {'customer': customer})

def customer_detail(request, pk):
    customer = Customer.objects.get(pk=pk)
    return render(request, 'customers/customer_detail.html', {'customer': customer})

def customer_autocomplete(request):
    if 'term' in request.GET:
        term = request.GET.get('term')
        customers = Customer.objects.filter(name__icontains=term)
        names = list(customers.values_list('name', flat=True))
        return JsonResponse(names, safe=False)
    return JsonResponse([], safe=False)