import csv
import os
from datetime import datetime

from api.models import (
    Address, Property,
    State, ZillowInformation)

from django.core.management.base import BaseCommand

from djangorest.settings import DATA_ROOT


class Command(BaseCommand):
    """
    A command that ingest csv data and build State,
    Address, ZillowInformation and Property objects out of
    the data.
    """

    def add_arguments(self, parser):
        # Sample path is 'csv/challenge_data.csv'
        parser.add_argument('path', type=str, help="The path of the data file")

    def handle(self, *args, **kwargs):
        file_path = kwargs['path']
        path = os.path.join(
            DATA_ROOT, file_path)
        with open(path) as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                # Get state from data.
                state = "N/A"
                try:
                    state = State.objects.get(
                        abbreviation=row[-2])
                except State.DoesNotExist:
                    pass

                # Create or get address from data.
                new_address, created = Address.objects.get_or_create(
                    line1=row[-4],
                    line2="",
                    city=row[-3],
                    state=state,
                    postal_code=row[-1])

                # Create or get zillow information from data.
                new_zinfo, created = ZillowInformation.objects.get_or_create(
                    zillow_id=row[18],
                    link=row[7],
                    rent_est=str_to_int(row[11]),
                    rent_est_last_updated=str_to_date(row[12]),
                    price_est=str_to_int(row[16]),
                    price_est_last_updated=str_to_date(row[17]),)

                # Create or get property information from data.
                new_property, created = Property.objects.get_or_create(
                    zillow=new_zinfo,
                    address=new_address,
                    area_unit=row[0],
                    bathrooms=str_to_float(row[1]),
                    bedrooms=str_to_int(row[2]),
                    home_size=str_to_int(row[3]),
                    home_type=row[4],
                    price=row[8],
                    price_last_sold=str_to_int(row[6]),
                    date_last_sold=str_to_date(row[5]),
                    rent=str_to_int(row[10]),
                    property_size=str_to_int(row[9]),
                    tax_value=str_to_float(row[13]),
                    tax_year=str_to_int(row[14]),
                    year_built=str_to_int(row[15]),)


def str_to_date(string):
    date = None
    if string:
        try:
            date = datetime.strptime(
                string, "%m/%d/%Y").strftime("%Y-%m-%d")
        except ValueError:
            pass
    return date


def str_to_int(string):
    result = 0
    if string.strip():
        try:
            result = int(string)
        except ValueError:
            pass
    return result


def str_to_float(string):
    result = 0.0
    if string.strip():
        try:
            result = float(string.strip())
        except ValueError:
            pass
    return result
