from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from quotes.models import QuoteItem, Quote  # ✅ Using your existing models



from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
@login_required
def dashboard_view(request):
    # ✅ Start with all quote items
    items = QuoteItem.objects.select_related('quote', 'product')

    # Initialize filters
    start_date, end_date = None, None
    date_range = request.GET.get('date_range')
    customer_name = request.GET.get('customer_name')

    # ✅ Filter 1: Date range
    if date_range:
        dates = date_range.split(' to ')
        if len(dates) == 2:
            start_date, end_date = dates
            items = items.filter(quote__created_at__date__range=[start_date, end_date])

    # ✅ Filter 2: Customer name
    if customer_name:
        items = items.filter(quote__customer_name=customer_name)

    # ✅ Aggregate Top 10 products by quantity
    top_products = (
        items.values('product__product_code', 'product__product_description')
        .annotate(total_qty=Sum('quantity'))
        .order_by('-total_qty')[:10]
    )

    labels = [p['product__product_code'] for p in top_products]
    data = [p['total_qty'] for p in top_products]

    # ✅ Dropdown list of customers
    customers = Quote.objects.values_list('customer_name', flat=True).distinct()

    return render(request, 'accounts/dashboard.html', {
        'labels': labels,
        'data': data,
        'customers': customers,
        'date_range': date_range,
    })
