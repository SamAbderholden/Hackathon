import requests

def get_data(zipcode, plan):
    endpoint = "https://apims.kaiserpermanente.org/kp/esb-envlbl/prod/care/pnl/doctorslocations-bff/v2/facilities/search"
    headers = {"x-region": "COL",
        "Cookie": "SSSC=874.G7334038403425591100.1|76399.2475417:78706.2532202:78942.2538485:79092.2542915:79093.2542919:79244.2547703:79254.2547942:79321.2549711:79423.2552745:79463.2553742:79543.2555920:79564.2556452:79575.2556737:80215.2573855:80298.2575578:80409.2578173:80515.2581139; KPSessionId=20f0630604b6191e3e1ccf7f6f12d87b94fd2b72cbd519821c6; HSESSIONID=20f0630604b6191e3e1ccf7f6f12d87b94fd2b72cbd519821c6; kp-visitor-id=KPPE7b6a41d14806c062c397043bd5b17903; S=2; kpLanguage=en-US; AMCVS_9644AD4E5628B1ED7F000101%40AdobeOrg=1; TS01cc593e=019761c73c4f03d9fa2ba99a650005434f6a3e53e2d259bfe45866553f4e183657a03b30ed0223234d20402ad450328f2866cd6f47; rxVisitor=1707588883359N3DSAE3529EBGCCFPISLLLMBN6O1876L; dtSa=-; rxvt=1707590706292|1707588883361; dtPC=32$588906232_142h-vBAMJGLWUBAFCIFUKMPIIPDVNVPGILFAG-0e0; ImpSessionRoP=COL; AMCV_9644AD4E5628B1ED7F000101%40AdobeOrg=179643557%7CMCIDTS%7C19764%7CMCMID%7C33038842159004050376325947639613438665%7CMCOPTOUT-1707596115s%7CNONE%7CvVersion%7C5.5.0; dtCookie=v_4_srv_35_sn_F31F1DBAF52F2C97A9787BABDFFBBD4D_perc_100000_ol_0_mul_1_app-3Aea7c4b59f27d43eb_0_app-3A9998adb6b210c2b7_0_app-3A2244804940fc3be6_0; TS01de35ba=019761c73ce44dc7dffc06c8dac98e035954a6fd8dd259bfe45866553f4e183657a03b30ed7ec6ca7c75d1c27c995d58c281bdcd66f450e597b175370e2c9e17589d50d99a; SSID=CQAr-B0AAAAAAAASvcdlPF9BDRK9x2UBAAAAAAAAAAAAEr3HZQDVzQ; SSRT=0L3HZQQBAA"}
    payload = {"searchRequest": {"maxResults": 200, "pageSize": 20, "criteria": {"searchQuery": "Urgent Care", "searchType": "facility", "zipCode": zipcode"}, 
                                 "filters": [{"id": "distance_label", "value": "0:11"}, {"id": "department_type_label", "value": "Urgent Care"}, {"id": "distance_label", "value": "0:11"}, {"id": "department_type_label", "value": "Urgent Care"}, {"id": "health_plan_label", "value": plan}, {"id": "facilitytype_label", "value": "Urgent Care Center"}]}}
    response = requests.post(endpoint, json=payload, headers=headers)
    data = response.json()
    print(data)
    urgent_cares = []
    for urgent_care in data["entries"]:
        location = {}
        location["name"] = urgent_care["name"]
        location["street"] = urgent_care["address"]["street"]
        location["city"] = urgent_care["address"]["city"]
        location["state"] = urgent_care["address"]["state"]
        location["zip"] = urgent_care["address"]["zip"]
        location["phone"] = urgent_care["phones"][0].split("|")[-1]
        location["lat"] = urgent_care["coordinates"]["lat"]
        location["lng"] = urgent_care["coordinates"]["lng"]
        print(location)
        urgent_cares.append(location)

    return urgent_cares
        



if __name__  == "__main__":
    get_data()