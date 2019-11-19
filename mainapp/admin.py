from django.contrib import admin
from mainapp.models import (
    Territory,
    City,
    Office,
    IndicatorGroup,
    IndicatorType,
    Indicator
)

admin.site.register(Territory)
admin.site.register(City)
admin.site.register(Office)
admin.site.register(IndicatorGroup)
admin.site.register(IndicatorType)
admin.site.register(Indicator)

