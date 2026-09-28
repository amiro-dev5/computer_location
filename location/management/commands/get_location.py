import socket
import platform
import requests
from django.core.management.base import BaseCommand


import socket
import platform
import requests

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Get computer information"

    def handle(self, *args, **options):
        # Computer information
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        operating_system = platform.system()
        machine = platform.machine()

        # Public IP
        public_ip = requests.get(
            "https://api.ipify.org",
            timeout=5
        ).text

        # Approximate location from public IP
        location_data = requests.get(
            f"https://ipwho.is/{public_ip}",
            timeout=5
        ).json()

        # Display information
        self.stdout.write("")
        self.stdout.write("========================================")
        self.stdout.write("        COMPUTER LOCATION INFO")
        self.stdout.write("========================================")

        self.stdout.write(f"Computer Name : {hostname}")
        self.stdout.write(f"Local IP      : {local_ip}")
        self.stdout.write(f"Public IP     : {public_ip}")
        self.stdout.write(f"Operating OS  : {operating_system}")
        self.stdout.write(f"Machine Type  : {machine}")

        self.stdout.write("----------------------------------------")

        self.stdout.write(
            f"Country       : {location_data.get('country')}"
        )
        self.stdout.write(
            f"City          : {location_data.get('city')}"
        )
        self.stdout.write(
            f"Latitude      : {location_data.get('latitude')}"
        )
        self.stdout.write(
            f"Longitude     : {location_data.get('longitude')}"
        )

        self.stdout.write("========================================")
        self.stdout.write("")