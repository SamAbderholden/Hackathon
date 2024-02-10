import requests

url = "https://hcpdirectory.cigna.com/web/public/consumer/directory/search"

# Define the headers
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Access-Control-Request-Headers": "x-c1agk3na-a,x-c1agk3na-b,x-c1agk3na-c,x-c1agk3na-d,x-c1agk3na-f,x-c1agk3na-z",
    "Access-Control-Request-Method": "GET",
    "Connection": "keep-alive",
    "Host": "p-hcpdirectory-waf.hcpdirectory.cigna.com",
    "Origin": "https://hcpdirectory.cigna.com",
    "Referer": "https://hcpdirectory.cigna.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

# Define the payload (query parameters)
params = {
    "consumerCode": "HDC001",
    "searchTerm": "Urgent Care Facility",
    "providerGroupCodes": "O",
    "medicalProductCode": "HMO",
    "medicalNetworkCode": "CO801",
    "dentalProductCode": "ADP",
    "pharmacyProductCode": "RX0100",
    "pharmacyNetworkCode": "0100",
    "behavioralProductCode": "MHSR",
    "behavioralNetworkCode": "6",
    "specialtyCode": "UC",
    "city": "Arvada",
    "stateCode": "CO",
    "country": "US",
    "zipCode": "80403",
    "searchLocation": "Arvada, CO 80403",
    "latitude": "39.833",
    "longitude": "-105.337",
    "formattedAddress": "Arvada, CO 80403",
    "searchCategoryType": "place-of-care",
    "categoryId": "91121",
    "fields": "providers,sortTypes,contextMessages,disclaimerCodes,alertCode",
    "limit": "20",
    "channel": "public"
}

# Send the GET request with headers and params
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Process the response data here
    print(response.json())
else:
    print("Request failed with status code:", response.status_code)
