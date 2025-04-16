from django.contrib import admin
from .models import Quote, QuoteItem

class QuoteItemInline(admin.TabularInline):
    model = QuoteItem
    extra = 1

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'created_at']
    inlines = [QuoteItemInline]
