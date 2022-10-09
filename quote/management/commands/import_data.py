"""
Import data
"""

from django.core.management.base import BaseCommand

class Command(BaseCommand):

    help = 'Import data on docker spinup'
    def handle(self, *args, **options):
        import urllib.request
        import json

        backup_url = 'https://glitch-backup.s3.amazonaws.com/quotes.backup.json'

        with urllib.request.urlopen(backup_url) as response:
            data = response.read()
            with open ('quote_import_data.json', 'w') as outfile:
                outfile.write(data.decode())
