from django.db import models
from django.utils.translation import gettext_lazy as _


class SolarYield(models.Model):
    class YieldBand(models.TextChoices):
        LOW = 'LO', _('Low')
        MID  = 'MI', _('Mid')
        HIGH = 'HI', _('High')
        UPPER = 'UP', _('Upper')
    country = models.CharField(default="de")
    date = models.DateField()
    zip_code_suffix = models.SmallIntegerField() 
    zip_code_prefix = models.SmallIntegerField()
    year = models.SmallIntegerField()
    band = models.CharField(
        max_length=2,
        choices=YieldBand.choices,
    )
    value = models.FloatField()