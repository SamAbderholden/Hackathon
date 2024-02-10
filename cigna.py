import requests

import requests

url = "https://hcpdirectory.cigna.com/web/public/consumer/directory/search"
params = {
    "consumerCode": "HDC001",
    "country": "US",
    "specialtyCode": "UC",
    "searchTerm": "Urgent Care Facility",
    "stateCode": "CO",
    "city": "Lakewood",
    "zipCode": "80401"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    try:
        data = response.json()
        # Now you can parse the 'data' variable to extract the locations
    except ValueError:
        print("Response content is not in JSON format:")
        print(response.text)
else:
    print("Error: Failed to retrieve data from the server. Status code:", response.status_code)




# Now you can parse the 'data' variable to extract the locations



#https://hcpdirectory.cigna.com/web/public/consumer/directory/search