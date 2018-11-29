from api.models import State

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Populate State model.
    """

    def handle(self, *args, **options):
        # Use California as an example for challenge csv data only.
        # Creation of objects of the rest of states is ommitted.
        new_state, created = State.objects.get_or_create(
            abbreviation='CA',
            name='California')
        placeholder, created = State.objects.get_or_create(
            abbreviation='N/A',
            name='N/A')
