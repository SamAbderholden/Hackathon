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
        "Akamai-Grn": "0.478d2117.1707612515.20c4b489",
        "Cache-Control":"no-cache,must-revalidate,max-age=0,no-store,private",
        "Content-Encoding": "gzip",
        "Content-Type": "application/json;charset=UTF-8",
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
        'Set-Cookie':"ak_bmsc=102F396F2D5A2C8BBF5D2DCE6655247F~000000000000000000000000000000~YAAQR40hFyFpPIWNAQAAgzOjlRYEppHQB62fEVJAftKDJkP38UgVoNayrDknPZTlOeNr3V9VaK+/Gqk8unv1lyjMk5Bti1kJtDfSQ/3s9p/ztqmXig9tceDRX8Td4YQIVEorxVAIVyovysLvk7Of9aje1iVeydV/b+LuTwximvi0fCdORnMyBEGKZy1W3ABMhVtt/cKpjqj9QqTW5yLO5DVEyicHyx89cugLDALIEqvGDffwWG4Q3epPEuW1FY2DcYsdXpjz1CBl5q+fkaO3908R/zJmf+mCmkNlxPxGKitjbyezG0H+wziQ6uxtH2ueyctnwmNTFH+XvgQ6LvEfFDplqCZbP7pTqbiWg6TxSG8fHkZipGVgrIOF+A26uTM3VJzrqbE2oNIH; Domain=.my.site.com; Path=/; Expires=Sun, 11 Feb 2024 02:48:35 GMT; Max-Age=7198; HttpOnly",
        'Referrer-Policy':'origin-when-cross-origin',
        
        "X-Requested-With":"XMLHttpRequest",
        "X-User-Agent":"Visualforce-Remoting",
        "Strict-Transport-Security": "max-age=63072000; includeSubDomains",
        "Vary":"Accept-Encoding",
        "X-Content-Type-Options":"nosniff",
        "X-Origin-Cache-Control":"no-cache,must-revalidate,max-age=0,no-store,private",
        "Sec-Ch-Ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        "Sec-Ch-Ua-Mobile": "?0",    
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/",
        "X-Requested-With": "XMLHttpRequest",
        "X-User-Agent": "Visualforce-Remoting"
        }
    payload = {
        "action":"ProviderSearchController",
        "method":"getProviders",
        
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
        "tid":2,
        "ctx":{
            "csrf":"VmpFPSxNakF5TkMwd01pMHhNMVF5TXpvME5UbzFNeTQzTnpWYSxMa2FFRERUc2JiRFJzelhkWHQ2VHZxM296bHZkVUtrSTRPUDdpUlAxQTVJPSxaR1V6TlRCaQ==",  
            "vid" : "0660H000005RR6P",
            "ns" : "",
            "ver":45,
            "authorization":"eyJub25jZSI6ImxRZndPSUJGVEZOUE82OFExUVB4UkxFcmRWUVlVc1o5TGR4UXZBUEFfWFlcdTAwM2QiLCJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IntcInRcIjpcIjAwRGkwMDAwMDAwSVB5UFwiLFwidlwiOlwiMDJHMEgwMDAwMDA0cWpjXCIsXCJhXCI6XCJ2ZnJlbW90aW5nc2lnbmluZ2tleVwiLFwidVwiOlwiMDA1MEgwMDAwMEQ0djd6XCJ9IiwiY3JpdCI6WyJpYXQiXSwiaWF0IjoxNzA3NjA4NzUzNzc3LCJleHAiOjB9.Q2lWUWNtOTJhV1JsY2xObFlYSmphRU52Ym5SeWIyeHNaWEl1WjJWMFVISnZkbWxrWlhKeg==.pOJtdjBY5K1UfYR_V76oZ10iQRQpBgtjjU1",
            }
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


