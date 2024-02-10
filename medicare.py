import requests
import re
from geopy.geocoders import Nominatim

zip_code = '80403'
geolocator = Nominatim(user_agent="my_app")
location = geolocator.geocode(zip_code)
if location:
    latitude = location.latitude
    longitude = location.longitude
    print(f"Latitude: {latitude}, Longitude: {longitude}")
else:
    print("Invalid zip code")


zip_code = '80403'
url = f'https://www.denverhealth.org/locations/search-results?location=&locationtype=urgent+care&services&services=&city=&zip={zip_code}&range=25'
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjIxNDQzNDMiLCJhcCI6IjQ2NDA3MTc5NCIsImlkIjoiZjA0Mzk2OWIwZWUxOWQ2ZSIsInRyIjoiNWZhYWUxYTFmN2E1YmE3YmE5M2FkMmU0NDVlNjAyMDAiLCJ0aSI6MTcwNzU5NDMxMDk2NCwidGsiOiIzOTAzMyJ9fQ==',
    'Traceparent': '00-5faae1a1f7a5ba7ba93ad2e445e60200-f043969b0ee19d6e-01',
    'Tracestate': '39033@nr=0-1-2144343-464071794-f043969b0ee19d6e----1707594310964',
    'Content-Type': 'application/json',
    'Content-Length': 216,
    'Origin': 'https://www.medicare.gov',
    'Referer': 'https://www.medicare.gov/care-compare/?providerType=Hospital',
    'Connection': 'keep-alive',
    'Host': 'www.medicare.gov',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Te': 'trailers',
}

payload = {
    "type":"Hospital",
    "filters":{"radiusSearch":{"coordinates":{"lon":-105.347036,"lat":39.904781},
    "radius":25},"emergencyServices":[true]},
    "page":1,
    "limit":15,
    "returnAllResults":false,
    "sort":["closest","rank","alpha"]}
r = requests.post('https://provider.bcbs.com/healthsparq/public/service/v4/search', json=payload, headers=headers)


if response.status_code == 200:
    print("Requested list:")
    data = (response.text)
    print(data)
else:
    print(f"Error: {response.status_code} - {response.text}")