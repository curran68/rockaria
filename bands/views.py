from django.shortcuts import render

# Create your views here.
# management/commands/export_bands_json.py
from django.core.management.base import BaseCommand
from django.core import serializers
from concerts.models import Band
import os

class Command(BaseCommand):
    help = 'Exports all band data to a JSON file'

    def handle(self, *args, **kwargs):
        bands = Band.objects.all()
        data = serializers.serialize('json', bands)

        output_dir = 'data_exports'
        os.makedirs(output_dir, exist_ok=True)
        file_path = os.path.join(output_dir, 'bands.json')

        with open(file_path, 'w') as f:
            f.write(data)

        self.stdout.write(self.style.SUCCESS(f'Bands exported to {file_path}'))
