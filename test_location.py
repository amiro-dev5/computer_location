import asyncio

from winrt.windows.devices.geolocation import Geolocator


async def main():
    locator = Geolocator()

    position = await locator.get_geoposition_async()

    latitude = position.coordinate.point.position.latitude
    longitude = position.coordinate.point.position.longitude

    print("Latitude :", latitude)
    print("Longitude:", longitude)


asyncio.run(main())