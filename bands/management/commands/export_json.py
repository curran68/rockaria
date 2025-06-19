import json
import os
from django.core.management.base import BaseCommand
from django.core import serializers
from bands.models import Concert  # Import your model

class Command(BaseCommand):
    help = "Export Concert data to JSON"

    def handle(self, *args, **kwargs):
        data = serializers.serialize("json", Concert.objects.all())
        file_path = os.path.join("exports", "concert_data.json")

        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as json_file:
            json_file.write(data)

        self.stdout.write(self.style.SUCCESS(f"Exported data to {file_path}"))