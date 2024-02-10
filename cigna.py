import requests
import BeautifulSoup

url = "https://hcpdirectory.cigna.com/web/public/consumer/directory/search"

# Send the GET request with headers and params
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
        # Process the response data here
        data = response.txt()
        soup = BeautifulSoup(response.content, "html.parser")
        print(data)
else:
    print("Request failed with status code:", response.status_code)
