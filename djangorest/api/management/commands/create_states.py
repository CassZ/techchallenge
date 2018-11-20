import os
import csv
from django.core.management.base import BaseCommand, CommandError
from djangorest.settings import STATIC_ROOT
from api.models import State


class Command(BaseCommand):
    """
    Populate State model.
    """

    def handle(self, *args, **options):
        # Use California as an example for challenge csv
        # data only. Cases of the rest of states are ommitted.
        new_state, created = State.objects.get_or_create(
            abbreviation='CA',
            name='California')
        placeholder, created = State.objects.get_or_create(
            abbreviation='N/A',
            name='N/A')