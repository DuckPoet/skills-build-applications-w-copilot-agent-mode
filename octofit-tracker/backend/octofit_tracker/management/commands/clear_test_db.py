# Clear the test database before running tests to avoid duplicate key errors.
from django.core.management.base import BaseCommand
from mongoengine.connection import get_db

class Command(BaseCommand):
    def handle(self, *args, **options):
        db = get_db()
        db.drop_database("test_octofit_db")