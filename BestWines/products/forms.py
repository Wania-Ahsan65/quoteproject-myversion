from django import forms
from .models import Product

class ProductUploadForm(forms.Form):
    file = forms.FileField(label="Upload Excel File")

class GeneralProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_code', 'product_description', 'category', 'size', 'abv', 'country']
        widgets = {
            'product_code': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'bg-gray-100 border rounded px-2 py-1 w-full'}),
            'product_description': forms.TextInput(attrs={'class': 'border rounded px-2 py-1 w-full'}),
            'category': forms.TextInput(attrs={'class': 'border rounded px-2 py-1 w-full'}),
            'size': forms.TextInput(attrs={'class': 'border rounded px-2 py-1 w-full'}),
            'abv': forms.NumberInput(attrs={'class': 'border rounded px-2 py-1 w-full'}),
            'country': forms.TextInput(attrs={'class': 'border rounded px-2 py-1 w-full'}),
        }

from django import forms
from .models import Product

class VariantProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # Include the 'id' field along with brand and cost_price.
        fields = ['id', 'brand', 'cost_price']
        widgets = {
            'id': forms.HiddenInput(),  # This field will be rendered as a hidden field.
            'brand': forms.TextInput(attrs={'class': 'border rounded px-2 py-1 w-full'}),
            'cost_price': forms.NumberInput(attrs={'class': 'border rounded px-2 py-1 w-full'}),
        }


