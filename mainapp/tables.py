import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from .models import Indicator


class IndicatorTable(tables.Table):

    id = tables.Column()
    type = tables.Column(verbose_name=_('Indicator'))
    value = tables.Column(verbose_name=_('Value'))
    date = tables.Column(verbose_name=_('Month'))
    office = tables.Column(verbose_name=_('Office'))
    group = tables.Column(accessor='type.group',
                          verbose_name=_('Indicators group'))
    territory = tables.Column(accessor='office.city.territory',
                              verbose_name=_('TO'))
    city = tables.Column(accessor='office.city', verbose_name=_('City'))

    class Meta:
        model = Indicator
        template_name = "mainapp/indicator.html"
        attrs = {"class": "paleblue table"}
        exclude = ('id', )
        sequence = ("date", "territory", "city", "office", "group", "type",
                    "value")
