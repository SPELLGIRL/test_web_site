import pandas as pd
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from django_tables2.export.views import ExportMixin

from .filters import IndicatorFilter
from .models import Indicator
from .tables import IndicatorTable


class FilteredMainView(ExportMixin, SingleTableMixin, FilterView):
    table_class = IndicatorTable
    model = Indicator
    template_name = "mainapp/indicator.html"

    filterset_class = IndicatorFilter

    export_formats = ("csv", "xls")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table = self.get_table(**self.get_table_kwargs())
        context[self.get_context_table_name(table)] = table
        df = pd.DataFrame(((obj.date, obj.office.city.territory.name,
                            obj.type.name, obj.value)
                           for obj in self.get_table_data()),
                          columns=('date', 'to', 'type', 'value'))
        df = df.sort_values('date').groupby(
            ['to', 'type', 'date']).agg('sum').groupby(
            ['to',
             'type']).agg(lambda x: round(100 * x.iloc[-1] / x.iloc[0]))
        context['result_table'] = df.to_html(classes='color_table')
        return context

    def get_queryset(self):
        return super().get_queryset().select_related()

    def get_table_kwargs(self):
        return {"template_name": "django_tables2/bootstrap.html"}
