#GET /1782/na.jsonp?network_id=1782&js_version=4.30.6&tag_id=1782/2624640718&request_data_shared_params={"utm_medium":"organic","utm_source":"google","invoca_id":"i-837cc262-d521-41c3-83b6-824d3125ae96","calling_page":"https://www.denverhealth.org/locations/search-results?location=Adult+Urgent+Care+Center&locationtype=&services=&city=&zip=80403&range=25","Entry_Page":"https://www.denverhealth.org/locations/search-results?location=Adult+Urgent+Care+Center&locationtype=&services=&city=&zip=80403&range=25","gclid":null,"invoca_caller_language":null,"keyword":null,"msclkid":null,"profile_name":null,"utm_campaign":null,"utm_content":null,"g_cid":"1193843539.1707583605"}&client_messages={}&client_info={"url":"https://www.denverhealth.org/locations/search-results?location=Adult+Urgent+Care+Center&locationtype=&services=&city=&zip=80403&range=25","referrer":"https://www.denverhealth.org/locations/search-results","cores":16,"platform":"MacIntel","screenWidth":1792,"screenHeight":1120,"language":"en-US"}&jsoncallback=json_rr2& HTTP/1.1

import requests
import re


zip_code = '80403'
url = f'https://www.denverhealth.org/locations/search-results?location=&locationtype=urgent+care&services&services=&city=&zip={zip_code}&range=25'
headers = {
    'Host': 'www.denverhealth.org',
    'Cookie': 'website#lang=en; ASP.NET_SessionId=2kozmb0nmri2j2cob1obtcbw; SC_ANALYTICS_GLOBAL_COOKIE=aba3316a3ebf46e09455db90a4c20438|True; addevent_track_cookie=d915a809-29b3-4cd0-c220-4d41d33c91a9; _gcl_au=1.1.1176390085.1707583604; _ga_484V9EBXC6=GS1.1.1707583604.1.0.1707583604.60.0.0; _ga=GA1.2.1193843539.1707583605; _uetsid=f94dbfe0c83311eebcb91fc74821a210; _uetvid=f94db220c83311ee945039c8f9139569; _scid=72f3c640-7618-4dc9-bbdd-47d18d30ca27; _scid_r=72f3c640-7618-4dc9-bbdd-47d18d30ca27; invoca_session=%7B%22ttl%22%3A%222024-03-11T15%3A46%3A47.372Z%22%2C%22session%22%3A%7B%22utm_medium%22%3A%22organic%22%2C%22utm_source%22%3A%22google%22%2C%22invoca_id%22%3A%22i-837cc262-d521-41c3-83b6-824d3125ae96%22%7D%2C%22config%22%3A%7B%22ce%22%3Atrue%2C%22fv%22%3Afalse%7D%7D; _sctr=1%7C1707548400000; _gid=GA1.2.27562982.1707583607; _dc_gtm_UA-4027206-1=1; __qca=P0-69337206-1707583607291',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.denverhealth.org/locations',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Te': 'trailers',
    'Connection': 'close'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Requested list:")
    data = (response.text)
    print(data)
else:
    print(f"Error: {response.status_code} - {response.text}")

response_text = '''
<div class="list-results__content-block">
    Adult Urgent Care Center<br/>660 N. Bannock St., Pavilion L, Floor 1<br/>Denver, CO 80204
</div><div class="list-results__content-block">

'''

# Find the location details
location_details = re.findall(r'<div class="list-results__content-block">(.+?)<br/>|<br/>(.+?)</div>\n<div class="list-results__content-block">', data)
print(location_details)


