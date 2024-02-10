import requests

def get_data(zipcode, plan):
    #https://healthy.kaiserpermanente.org/colorado/doctors-locations#/facility-results?zipcode=80401&keyword=Urgent%20Care
    #"search"
    try:
        endpoint = "https://apims.kaiserpermanente.org/kp/esb-envlbl/prod/care/pnl/doctorslocations-bff/v2/facilities/search"
        headers = {"x-region": "COL", "x-correlationid": "2882cb20-2e9c-43bb-b848-0c79726b33db", "X-Appname": "doctors-locations",
            "Cookie": "KPSessionId=20f0630604b6191e3e1ccf7f6f12d87b94fd2b72cbd519821c6; HSESSIONID=20f0630604b6191e3e1ccf7f6f12d87b94fd2b72cbd519821c6; kp-visitor-id=KPPE7b6a41d14806c062c397043bd5b17903; S=2; kpLanguage=en-US; AMCVS_9644AD4E5628B1ED7F000101%40AdobeOrg=1; rxVisitor=1707588883359N3DSAE3529EBGCCFPISLLLMBN6O1876L; dtSa=-; rxvt=1707590706292|1707588883361; dtPC=32$588906232_142h-vBAMJGLWUBAFCIFUKMPIIPDVNVPGILFAG-0e0; SSID=CQBtOB0AAAAAAAASvcdlPF9BDRK9x2UCAAAAAAAAAAAATNjHZQDVzQ; SSSC=874.G7334038403425591100.2|0.0; ImpSessionRoP=COL; dtCookie=v_4_srv_35_sn_F31F1DBAF52F2C97A9787BABDFFBBD4D_perc_100000_ol_0_mul_1_app-3Aea7c4b59f27d43eb_0_app-3A9998adb6b210c2b7_0_app-3A2244804940fc3be6_0; TS01cc593e=01baeb76219151ffe3b692361b24609bd01317c99dfde04196b41534cfcf784c9f6dd665c63508ff4cfc5408bbede3e6dfffb04e0f; TS01de35ba=01baeb7621e21ed6616f7f174c3b69d09278cbe712fde04196b41534cfcf784c9f6dd665c6fa2e8295c8b5c5678b0c7e1c3a06de5b5d41ef6602ef91ab719ed5735b65805c; SSRT=8-DHZQQBAA; AMCV_9644AD4E5628B1ED7F000101%40AdobeOrg=179643557%7CMCIDTS%7C19764%7CMCMID%7C33038842159004050376325947639613438665%7CMCOPTOUT-1707605266s%7CNONE%7CvVersion%7C5.5.0"}
        payload = {"searchRequest": {"maxResults": 200, "pageSize": 20, "criteria": {"searchQuery": "Urgent Care", "searchType": "facility", "zipCode": str(zipcode)}, 
                                    "filters": [{"id": "distance_label", "value": "0:11"}, {"id": "department_type_label", "value": "Urgent Care"}, {"id": "department_type_label", "value": "Urgent Care"}, {"id": "health_plan_label", "value": plan}]}}
        response = requests.post(endpoint, json=payload, headers=headers)
        data = response.json()
        print(data)
        urgent_cares = []
        for urgent_care in data["entries"]:
            location = {}
            location["fullName"] = urgent_care["name"]
            location["address"] = {"line1": urgent_care["address"]["street"],
                                "city": urgent_care["address"]["city"],
                                "state": urgent_care["address"]["state"],
                                "zip": urgent_care["address"]["zip"]}
            location["phone"] = urgent_care["phones"][0].split("|")[-1]
            location["latitude"] = urgent_care["coordinates"]["lat"]
            location["longitude"] = urgent_care["coordinates"]["lng"]
            print(location)
            urgent_cares.append(location)

        return urgent_cares
    except:
        return 0
        



if __name__  == "__main__":
    get_data(80401, "Choice PPO")