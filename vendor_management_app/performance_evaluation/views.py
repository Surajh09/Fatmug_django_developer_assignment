from rest_framework import viewsets
from .models import HistoricalPerformance
from .serializers import HistoricalPerformanceSerializer

class HistoricalPerformanceViewSet(viewsets.ModelViewSet):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
    