import requests
import re

zip_code = '80403'


url = f'https://www.medicare.gov/api/care-compare/provider/'
headers = {
'Accept':'application/json, text/plain, */*',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'en-US,en;q=0.9',
'Connection':'keep-alive',
'Content-Type': 'application/json',
'Cookie':'optimizelyEndUserId=b5592117a6d43a00cfd0c765e5030000d17d0500; bm_sz=0A0C4205E0EB76C913A9D33F25C8A900~YAAQtVkhF1CpoIONAQAAfayHlBbxEF1NPMozvbsOy1hB1ienZvAtIReFyUJ4pBxjIackBOruwmk6romxLzbyfVJYDHK60LSnt8Fd+IXCz0cUhNjs7mIRv+gadS97bZGXG5EeGFrtxtV+cQu4hs2BETDWRCz7UsOipppyuCEicSRMNlq/oPtSYREHon72oG5O5HYdayK8UA8w4qwAl5vj8fJydPcgU9bbgqw3/kBM0lyjhProHiJ4hFCBnzFDQirs5kDiKexIwBd7cOEG6N9DjUWtmeDoCdQ4mNP0deacboQMrWy1uwWTr4O4hitTjFzye7cwT6GuSA6R1N4hQxDtCQ==~3491381~3425335; _ga=GA1.2.1503987118.1707593935; CONSENTMGR=c1:1%7Cc2:1%7Cc3:1%7Cc4:1%7Cc5:1%7Cc6:1%7Cc7:1%7Cc8:1%7Cc9:1%7Cc10:1%7Cc11:1%7Cc12:1%7Cc13:1%7Cc14:1%7Cc15:1%7Cts:1707593937810%7Cconsent:true; kndctr_0600459D5DBAF9400A495E7C_AdobeOrg_identity=CiY0NDM0OTc4MzE4NTg5NjkxMDAzMDU1OTcxNjY0NDMzNDc5NjM3MVIQCJDynqTZMRgBKgNPUjIwAfABkPKepNkx; AMCV_0600459D5DBAF9400A495E7C%40AdobeOrg=MCMID|44349783185896910030559716644334796371; QuantumMetricUserID=0b17c56670c8a383026aff9d037d6a38; QuantumMetricSessionID=f3514e3bcb35a1c037c3747d84a47ec4; _abck=C9854214FA347DEAD054C3E99E871774~0~YAAQtVkhF6+GsIONAQAA5MTelAtinecyscAZ4GmJSBRRwXhv3I3cakRUJCrG4MqykVoHKASzIuoVFZORPMIToJGxVTyFa7graqjrg1G6tLdR4ZpMDnsWLy/Po192mrhft2wFL9pjtGSo7RH243cwGGgL0FwwpVzbVvlt8x0xPvVlfJaMci4qgAte73VRd9Zm1tFrTkSGKTDYCiMVfVLa2CnAF03c0RK1vzM3Fhyo/d+3w8vdnzlbnKOtXFyXeyiapXn25xQxSNCaPqhnMWLn3NIC/ahSGo38jmdbiGbM3mxuzPsaR1zyd0EhtKmtB6I0dZl9gmbOPa+V08cJOVPeFfbBSHEJqJCLB4vpOJHZHbeYGBqNK+4CMqK425AW23mZw6Dq5NgS/o7QGKfLRFwETMIm9qAcZ2FFmyo=~-1~-1~1707603237; kndctr_0600459D5DBAF9400A495E7C_AdobeOrg_cluster=or2; ak_bmsc=9B4688545571F05CAB1B527223812D3E~000000000000000000000000000000~YAAQtFkhF0XYvmiNAQAAH0YDlRYMqME8m9D6tWPkhWHg/SVntuvdneIw6iW8CShx+XU1Rit/W424LW+th1iXwKZ36pvMR70vAmIUIM/tnA8f+mLSm1bR9URvFEAuMlTukhxcbMecs/qG8RSAv6zF3IhPiuzDuWj9jvMk3COkXEmvftewA68w90cX0pqsoJznnb2bLW2q7v+PBzsu80+EN5Mkpjx2DIEB9AolWh86DKwedaxlVkVATyrs7sFMUViMdTiFdUH/fGfaknfNcA5XJewYKL4AxEeKrRCHWg9g1jwNCERXDJrwdsIW/UVnd+JY5MQdzCL+KV1SYvFpczOkX6wZbvPShWg8QntcipRV+gaiFvON7yVfxU540c7qiT/5n0WMX9cZHNQAtA==; utag_main=v_id:018d9487b393000a88d37410109a05075004a06d00b78$_sn:4$_se:6$_ss:0$_st:1707603945839$dc_visit:4$ses_id:1707601938203%3Bexp-session$_pn:2%3Bexp-session$dc_event:5%3Bexp-session; akavpau_default=1707602446~id=0e82a2a545ddef530ed082475973c863; bm_sv=3AF6DA382CE64CA76E2151AD7251704C~YAAQtFkhFxYov2iNAQAAtvMElRazNwBJxr7QUpJLvXHrUvox2xTLtfkG9q+8r35w8hjTWYfvEKr0iDh0BGV88/FgXaJyFD8IldFGWjMIqdoLw4A9rcsL6XaS354W29rddo993CDq8SrCng42QapsyHEfRyhqul4pxz5Jgz5cDRyebM7I4Ajz+ZmkDV5ucSMv54eFXvojfXtCcZWdzEfgj5hut/v3GbS5RCHMCpEWiZ+HELOF9Mp/3KuxqCrOaT3jflQ=~1',
'Newrelic':'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjIxNDQzNDMiLCJhcCI6IjQ2NDA3MTc5NCIsImlkIjoiY2I5NTYxNzFmNjU4NDY5ZSIsInRyIjoiYTVjMjIxZGEzNTg2YjVmODgyNjA5MTIyMzBmNjA3MDAiLCJ0aSI6MTcwNzYwMjE0NjMxNCwidGsiOiIzOTAzMyJ9fQ==',
'Origin':'https://www.medicare.gov',
'Referer':'https://www.medicare.gov/care-compare/results/?searchType=Hospital&page=1&city=Golden&state=CO&zipcode=80403&radius=25&emergencyServices=true&sort=closest&tealiumEventAction=Landing%20Page%20-%20Search&tealiumSearchLocation=search%20bar%20-%20suggested%20search%20result',
}
payload = {
     "type":"Hospital",
    "filters":{"radiusSearch":{"coordinates":{"lon":-105.347036,"lat":39.904781},
    "radius":25},
    "emergencyServices":[True]},
    "page":1,"limit":15,"returnAllResults":False,
    "sort":["closest","rank","alpha"]
    }
response = requests.post(url, json=payload, headers=headers)
data = response.json()
print(data)
    
providers_list = []
for hospital in data['results']:
    
    name = hospital['name']
    address = hospital['hospital']['addressLine1']
    city = hospital['hospital']['addressCity']
    state = hospital['hospital']['addressState']
    zip_code = hospital['hospital']['addressZipcode']
    phone = hospital['hospital']['phone']
    latitude = hospital['lat']
    longitude = hospital['lon']

    print(f"Name: {name}")
    print(f"Address: {address}")
    print(f"City: {city}")
    print(f"State: {state}")
    print(f"Zip Code: {zip_code}")
    print(f"Phone: {phone}")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
    print()

    
    



