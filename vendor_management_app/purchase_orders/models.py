from django.db import models
from django.db.models import Count, Avg
from django.utils import timezone
from vendors.models import Vendor


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.po_number
    
    def calculate_on_time_delivery_rate(self):
        total_completed_orders = PurchaseOrder.objects.filter(vendor=self.vendor, status='completed').count()
        on_time_orders = PurchaseOrder.objects.filter(vendor=self.vendor, status='completed', delivery_date__lte=timezone.now()).count()
        if total_completed_orders == 0:
            return 0
        return (on_time_orders / total_completed_orders) * 100

    def calculate_quality_rating_avg(self):
        avg_quality_rating = PurchaseOrder.objects.filter(vendor=self.vendor, status='completed').aggregate(avg_rating=Avg('quality_rating'))['avg_rating']
        return avg_quality_rating or 0

    def calculate_average_response_time(self):
        response_times = PurchaseOrder.objects.filter(vendor=self.vendor, acknowledgment_date__isnull=False).annotate(response_time=models.F('acknowledgment_date') - models.F('issue_date')).aggregate(avg_response_time=Avg('response_time'))['avg_response_time']
        return response_times.total_seconds() / 60 if response_times else 0

    def calculate_fulfillment_rate(self):
        total_orders = PurchaseOrder.objects.filter(vendor=self.vendor).count()
        successful_orders = PurchaseOrder.objects.filter(vendor=self.vendor, status='completed').count()
        if total_orders == 0:
            return 0
        
        return (successful_orders / total_orders) * 100
