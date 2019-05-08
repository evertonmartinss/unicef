import django_filters

from mortalidade.models import Country, Mortality


class CountryFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Country
        fields = ['iso_code', 'country_name']

class MortalityFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Mortality
        fields = ['iso_code', 'median','year']