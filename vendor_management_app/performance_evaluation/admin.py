from django.contrib import admin
from .models import HistoricalPerformance

@admin.register(HistoricalPerformance)
class HistoricalPerformanceAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'date', 'on_time_delivery_rate', 'quality_rating_avg', 'fulfillment_rate')
    search_fields = ('vendor__name',)
    list_filter = ('date',)
