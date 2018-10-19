import csv

from django.core.management.base import BaseCommand, CommandError
from lottery.models import Registration

class Command(BaseCommand):
    help = 'Import registration emails into the registration database.'

    def add_arguments(self, parser):
        parser.add_argument('-s', '--separator',
                            dest='separator',
                            help='Field separator',
                            default=',')
        parser.add_argument('-e', '--email-pos',
                            dest='position',
                            help='Field position for the email, starts on 0')
        parser.add_argument('filename',
                            metavar='FILENAME',
                            nargs=1)

    def handle(self, *args, **options):
        with open(options['filename'], 'r') as origin:
            data_reader = csv.reader(origin, delimiter=options['separator'])
            for row in data_reader:
                email = row[options['position']]
                try:
                    Registration(email=email).save()
                except Exception:   # KILL ME!
                    # Assuming it happens 'cause there is an email registrered
                    # already
                    pass
