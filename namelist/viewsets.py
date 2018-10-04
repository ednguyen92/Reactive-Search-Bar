from rest_framework import viewsets, filters
from .models import Namelist
from .serializers import NamelistSerializer

class NamelistViewSet(viewsets.ModelViewSet):
    queryset = Namelist.objects.all()
    serializer_class = NamelistSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_id', 'name')