from django.db import models
from django.utils.translation import ugettext as _
from decimal import Decimal


class State(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    abbreviation = models.CharField(
        _('Abbreviation'), max_length=10, primary_key=True)

    class Meta:
        verbose_name = _("State")
        verbose_name_plural = _("States")

    def __str__(self):
        return self.name


class Address(models.Model):
    line1 = models.CharField(
        _("First Line of Address"), max_length=255)
    line2 = models.CharField(
        _("Second Line of Address"), max_length=255, blank=True)
    city = models.CharField(
        _("City"), max_length=255, blank=True)
    state = models.ForeignKey(
        _('State'), on_delete=models.CASCADE,)
    postal_code = models.CharField(
        _("Postal Code"), max_length=64, blank=True)

    def __str__(self):
        return self.line1


class ZillowInformation(models.Model):
    zillow_id = models.CharField(
       _("First Line of Address"),
       max_length=20, primary_key=True)
    link = models.CharField(
        _("Link"), max_length=2000, blank=True)

    rent_est = models.PositiveIntegerField(
        _("Zestimate Rent"), null=True, blank=True)
    rent_est_last_updated = models.DateField(
        _("Zestimate Rent Last Updated"), blank=True)

    price_est = models.PositiveIntegerField(
        _("Zestimate Price"), null=True, blank=True)
    price_est_last_updated = models.DateField(
        _("Zestimate Price Last Updated"), blank=True)

    def __str__(self):
        return self.zillow_id


class Property(models.Model):
    area_unit = models.CharField(
        _("Area Unit"), max_length=20)
    bathrooms = models.DecimalField(
        max_digits=5, decimal_places=1,
        blank=True, null=True)
    bedrooms = models.PositiveIntegerField(
        _("Bedrooms"), blank=True, null=True)
    home_size = models.PositiveIntegerField(
        _("Home Size"), blank=True, null=True)
    home_type = models.CharField(
        _("Home Type"), max_length=40,
        blank=True, null=True)
    price = models.PositiveIntegerField(
        _("Price"), blank=True)
    price_last_sold = models.PositiveIntegerField(
        _("Price Last Sold"), null=True, blank=True)
    date_last_sold = models.DateField(
        _("Date Last Sold"), null=True, blank=True)
    rent = models.PositiveIntegerField(
        _("Rent"), blank=True)
    property_size = models.PositiveIntegerField(
        _("Property Size"), blank=True, null=True)
    tax_value = models.PositiveIntegerField(
        _("Tax Value"), null=True, blank=True)
    tax_year = models.PositiveIntegerField(
        _("Tax Year"), null=True, blank=True)
    year_built = models.PositiveIntegerField(
        _("Year Built"), null=True, blank=True)
    address = models.ForeignKey(
        'Address', on_delete=models.CASCADE)
    zillow = models.OneToOneField(
        'ZillowInformation',
        null=True, blank=True,
        on_delete=models.CASCADE)

