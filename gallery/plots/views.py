from rest_framework import viewsets
from plots.serializers import PlotsSerializer
from plots.models import Plots


class PlotsViewSet(viewsets.ModelViewSet):
    queryset = Plots.objects.all()
    serializer_class = PlotsSerializer
