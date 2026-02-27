from django.core.management.base import BaseCommand
from djongo import connection

class Command(BaseCommand):
    help = 'Show collections and sample documents in octofit_db'

    def handle(self, *args, **options):
        db = connection.cursor().db_conn
        collections = db.list_collection_names()
        self.stdout.write('Collections: ' + ', '.join(collections))
        for name in collections:
            doc = db[name].find_one()
            self.stdout.write(f'Collection: {name}\nSample: {doc}\n')
