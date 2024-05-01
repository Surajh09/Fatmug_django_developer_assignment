from django.contrib import admin
from .models import Vendor

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'vendor_code', 'on_time_delivery_rate', 'fulfillment_rate')
    search_fields = ('name', 'vendor_code')