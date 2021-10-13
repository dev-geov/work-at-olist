"""
Read Csv Command.
"""

# External imports
from django.core.management.base import BaseCommand, CommandError
import pandas as pd
from pandas import DataFrame

# Internal imports
from library.models import Author


class Command(BaseCommand):
    """
    Class Command.
    """

    help = 'Read CSV file and save data into database.'

    def add_arguments(self, parser):
        """
        Add Argumnets method.

        [Inherits from BaseCommand]
        """

        parser.add_argument('--file', action='store')
    
    def save_author_from_dataframe(self, authors_df: DataFrame) -> int:
        """
        Save author from dataframe into database.

        :param author_df: Authors read from csv file in dataframe format.

        :returns: total authors read and saved on database.
        """

        authors_saved = 0

        for name in authors_df['name']:
            author = Author(name=name)
            try:
                author.save()
                authors_saved += 1
                self.stdout.write(self.style.SUCCESS(f'Author {name} saved on database.'))
            except:
                self.stdout.write(self.style.ERROR(f'Author {name} NOT saved on database.'))
        
        return authors_saved

    def handle(self, *args, **options):
        """
        Handle method.

        [Inherits from BaseCommand].
        """

        self.stdout.write(self.style.SUCCESS('Starting reading data from CSV file...'))
        if options.get('file'):
            try:
                file_path = options.get('file')
                file_df = pd.read_csv(file_path)
                total = self.save_author_from_dataframe(authors_df=file_df)
                self.stdout.write(self.style.SUCCESS(f'Successfully saved {total} authors.'))
            except:
                raise FileNotFoundError('No file found')
        self.stdout.write(self.style.SUCCESS('Successfully read CSV file and saved authors name'))