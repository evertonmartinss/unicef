from rest_framework import viewsets

from mortalidade.models import *
from nutricao.api.filters import PacienteFilter


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_class = CountryFilter

class MortalityViewSet(viewsets.ModelViewSet):
    queryset = Mortality.objects.all()
    serializer_class = MortalitySerializer
    filter_class = MortalityFilter

