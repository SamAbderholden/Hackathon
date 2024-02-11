import requests
import csv

def read_zip_coordinates(zip_code):
    with open('./static/zipToLoc.txt', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['ZIP'] == zip_code:
                return float(row['LAT']), float(row['LNG'])
    return None, None

def get_data(location):
    lat, long = read_zip_coordinates(location)
    url = f'https://peak.my.site.com/peak/apexremote'
    headers = {
        'Accept':'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Length': '1027',
        'Content-Type': 'application/json',
        'Cookie': 'CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1; BrowserId_sec=h0B0UshuEe6wt60MUtYWUg; pctrk=4eea2679-8fc6-4912-a05b-97af75e94544',
        'Origin': 'https://peak.my.site.com',
        'Referer': 'https://peak.my.site.com/peak/providersearchpage',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Set-Cookie':"ak_bmsc=127B035B1DA1A234EF1C1D48DEC3AFA1~000000000000000000000000000000~YAAQR40hF52gOoWNAQAA+dZ+lRa4TqDYB/G8dQhfDfpwZ5rRBGrbQuYuhXXM9JAMsnhjkWEacQFi9/f2Gs0MuD0cVhuK1+so0pmKjCItk/18loL5IWtb5eWxBgzFs23+YQpfzAPwvf6NhvRS2v3QceVve/MNWF/jU5LfcEk0I3/yb6Oly5F8p0oTFrkBcFV/YUq9iUILy3a6pfrjR9XozA6musP6zkJ1avPoMwoCjj5cZGW01I+td5h8ax1JOwAIMW22U9mRIwCrVD8SxBWD/66EZtmIpOyfhPnh6khNyQaPRZkMclkfwjbKmINZSSlCSkw4Y7NJ3XvsL8koEQlvJaHAwdtG6OXUyP8+QCFlZBOoJcQTB/B2De1NBzeyLnffTVhUq9HP8DRr; Domain=.my.site.com; Path=/; Expires=Sun, 11 Feb 2024 02:08:52 GMT; Max-Age=7198; HttpOnly",
        'Referrer-Policy':'origin-when-cross-origin'
        }
    payload = {
        "action":"ProviderSearchController",
        "method":"getProviders",
        "ver":"45",
        "vid" : "0660H000005RR6P",
        "data":[{"apexType":"c.ProviderSearchController.ProviderSearchFilters",
                 "selectedLatitude":lat,
                 "selectedLongitude":long,
                 "withinMiles":30,
                 "providerName":"",
                 "newPatients":False,
                 "providerType":"Urgent Care",
                 "healthPlan":"",
                 "specialtyType":"",
                 "waiverType":"",
                 "waiverServices":""},0],
        "type":"rpc",
        "ns":"",
        "tid":5,
        "ctx":{"csrf":"VmpFPSxNakF5TkMwd01pMHhNMVF5TXpvME5UbzFNeTQzTnpWYSxMa2FFRERUc2JiRFJzelhkWHQ2VHZxM296bHZkVUtrSTRPUDdpUlAxQTVJPSxaR1V6TlRCaQ=="},  
        "authorization":"eyJub25jZSI6ImxRZndPSUJGVEZOUE82OFExUVB4UkxFcmRWUVlVc1o5TGR4UXZBUEFfWFlcdTAwM2QiLCJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IntcInRcIjpcIjAwRGkwMDAwMDAwSVB5UFwiLFwidlwiOlwiMDJHMEgwMDAwMDA0cWpjXCIsXCJhXCI6XCJ2ZnJlbW90aW5nc2lnbmluZ2tleVwiLFwidVwiOlwiMDA1MEgwMDAwMEQ0djd6XCJ9IiwiY3JpdCI6WyJpYXQiXSwiaWF0IjoxNzA3NjA4NzUzNzc3LCJleHAiOjB9.Q2lWUWNtOTJhV1JsY2xObFlYSmphRU52Ym5SeWIyeHNaWEl1WjJWMFVISnZkbWxrWlhKeg==.pOJtdjBY5K1UfYR_V76oZ10iQRQpBgtjjU1",

        }
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    print(data)
    
    '''providers_list = []
    for hospital in data['results']:
        provider_info = {
            "fullName" : hospital['name'],
            "address" : {
                "line1": hospital['hospital']['addressLine1'],
                "city": hospital['hospital']['addressCity'],
                "state": hospital['hospital']['addressState'],
                "zip": hospital['hospital']['addressZipcode'],
            },
            "latitude": hospital['lat'],
            "longitude": hospital['lon'],
            "phone": hospital['hospital']['phone']
            } 
        providers_list.append(provider_info)
    return(providers_list)
        '''


if __name__  == "__main__":
    get_data("60048")
