from django_filters import FilterSet, DateFromToRangeFilter
from django_filters.widgets import RangeWidget
from django.utils.translation import gettext_lazy as _

from .models import Indicator


class CustomRangeWidget(RangeWidget):
    suffixes = ['gte', 'lt']


class IndicatorFilter(FilterSet):
    date = DateFromToRangeFilter(widget=CustomRangeWidget(attrs={
        'type': 'date',
        'class': 'datepicker'
    }))

    class Meta:
        model = Indicator
        fields = {
            'type': ['exact'],
            'office': ['exact'],
            'type__group': ['exact'],
            'office__city': ['exact'],
            'office__city__territory': ['exact'],
        }
