from django.db import models
from django.utils.translation import gettext_lazy as _


class Territory(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('territory name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("territories")


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('city name'))
    territory = models.ForeignKey(Territory,
                                  on_delete=models.CASCADE,
                                  related_name='cities')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("cities")


class Office(models.Model):
    number = models.PositiveIntegerField(verbose_name=_('office number'))
    city = models.ForeignKey(City,
                             on_delete=models.CASCADE,
                             related_name='offices')

    def __str__(self):
        return f'{self.number}'


class IndicatorGroup(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('group name'))

    def __str__(self):
        return self.name


class IndicatorType(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('indicator type'))
    group = models.ForeignKey(IndicatorGroup,
                              on_delete=models.CASCADE,
                              related_name='indicator_types')

    def __str__(self):
        return self.name


class Indicator(models.Model):
    type = models.ForeignKey(IndicatorType,
                             on_delete=models.CASCADE,
                             related_name='indicators')
    value = models.IntegerField()
    date = models.DateField()
    office = models.ForeignKey(Office,
                               on_delete=models.CASCADE,
                               related_name='indicators')

    def __str__(self):
        return f'{self.office}-{self.type}-{self.value}'
