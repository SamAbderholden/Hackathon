import requests
import re
import pgeocode

zip_code = '80403'
nomi = pgeocode.Nominatim('us')
a = nomi.query_postal_code(zip_code)
print(a['latitude'], a['longitude'])

url = f'https://www.denverhealth.org/locations/search-results?location=&locationtype=urgent+care&services&services=&city=&zip={zip_code}&range=25'
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjIxNDQzNDMiLCJhcCI6IjQ2NDA3MTc5NCIsImlkIjoiZjA0Mzk2OWIwZWUxOWQ2ZSIsInRyIjoiNWZhYWUxYTFmN2E1YmE3YmE5M2FkMmU0NDVlNjAyMDAiLCJ0aSI6MTcwNzU5NDMxMDk2NCwidGsiOiIzOTAzMyJ9fQ==',
    'Traceparent': '00-5faae1a1f7a5ba7ba93ad2e445e60200-f043969b0ee19d6e-01',
    'Tracestate': '39033@nr=0-1-2144343-464071794-f043969b0ee19d6e----1707594310964',
    'Content-Type': 'application/json',
    'Content-Length': '216',
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
    "filters":{"radiusSearch":{"coordinates":{"lon":a['longitude'],"lat":a['latitude']},
    "radius":25},"emergencyServices":[True]},
    "page":1,
    "limit":15,
    "returnAllResults":False,
    "sort":["closest","rank","alpha"]}
response = requests.post('https://www.medicare.gov/care-compare/?providerType=Hospital', json=payload, headers=headers)




if response.status_code == 200:
    print("Requested list:")
    data = (response.json())
    print(data)
else:
    print(f"Error: {response.status_code} - {response.text}")