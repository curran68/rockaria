import os
from django.core.management.base import BaseCommand
from django.core import serializers
from bands.models import Band, Concert

class Command(BaseCommand):
    help = "Export Band and Concert data to JSON"

    def handle(self, *args, **kwargs):
        data = serializers.serialize("json", list(Band.objects.all()) + list(Concert.objects.all()))
        file_path = os.path.join("exports", "concert_data.json")

        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as json_file:
            json_file.write(data)

        self.stdout.write(self.style.SUCCESS(f"Exported Band and Concert data to {file_path}"))

