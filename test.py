import requests

plan = 'POS'
location = '80401'
payload = {"guid":"65461f76-dffa-4be1-9f64-8049edba3d5b","languageCode":"EN","alphaPrefix":plan,"isPromotionSearch":True,"key":"Urgent Care","location":location, "query":"Urgent Care", "radius":25}
headers = {"Cookie": "trace-session-id=4464e18a-c05c-461a-b2a1-4344a096ff50; SESSION=YjI3OGExMTItMjA3YS00NDQ0LWE5N2QtZDhlNmRkMzRhMmFj; visit_num=1; prev_page_ppv=50; utag_main=v_id:018d9133a4e7001e89c6b3b96bbf0506f009006700bd0$_sn:1$_se:37$_ss:0$_st:1707540708761$ses_id:1707538097384%3Bexp-session$_pn:2%3Bexp-session$_ga:018d9133a4e7001e89c6b3b96bbf0506f009006700bd0"}
r = requests.post('https://provider.bcbs.com/healthsparq/public/service/v4/search', json=payload, headers=headers)
#print(r.json())

data = r.json()

for provider in data["providerResults"]:
    print(provider["provider"]["fullName"], provider["location"]["address"]["line1"], provider["location"]["address"]["city"], provider["location"]["address"]["state"], provider["location"]["address"]["zip"], provider["location"]["phone"])

