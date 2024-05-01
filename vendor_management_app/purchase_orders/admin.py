from django.contrib import admin
from .models import PurchaseOrder

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('po_number', 'vendor', 'order_date', 'status')
    search_fields = ('po_number', 'vendor__name')
    list_filter = ('status', 'order_date')
    