from csv import DictReader
from django.core.management.base import BaseCommand

# Import the model
from accounts.models import Countries

ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the country data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from countries.csv"

    def handle(self, *args, **options):

        # Show this if the data already exist in the database
        if Countries.objects.exists():
            print('country data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return

        # Show this before loading the data into the database
        print("Loading countries data")

        # Code to load the data into database
        for row in DictReader(open('./countries.csv')):
            country = Countries(country_name=row['name'])
            country.save()