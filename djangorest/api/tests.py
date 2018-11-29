from api.models import Property

from django.core.management import call_command

from django.test import TestCase


class IngestPropertyCSVTestCase(TestCase):
    def test_command(self):
        """
        Test ingest_csv_data command.
        """
        call_command('create_states')
        call_command('ingest_property_csv')

        self.assertEquals(
            1, Property.objects.filter(
                zillow_id="19866015").count())
        self.assertEquals(
            448, Property.objects.all().count())
