import requests

def get_data(zipcode, plan):
    #https://healthy.kaiserpermanente.org/colorado/doctors-locations#/facility-results?zipcode=80401&keyword=Urgent%20Care
    #"search"
    try:
        import requests

        endpoint = "https://api2.aetna.com/healthcare/prod/v3/publicdse_providersearch"
        headers = {
            "Content-Type": "application/json",
            'X-Backside-Transport': 'OK OK',
            'X-Global-Transaction-Id': 'abc6a0c865c7ef51901eb921',
            'X-Original-Http-Status-Code': '200',
            'X-Ratelimit-Limit': 'name=rate-limit,33600;',
            'X-Ratelimit-Remaining': 'name=rate-limit,33584;',
            'X-Ibm-Client-Id': '92e66fe9-52de-4cf3-8966-5860450c4f56'
        }

        params = {
            'searchText': 'Urgent Care',
            'distance': '25',
            'productIdentifier': '~MPPO',
            'state': 'CO',
            'listFieldSelections': 'acceptedVersion_wjtk0,affiliations',
            'postalCode': zipcode,
            'pipeName': 'Open Choice PPO',
            'siteId': 'dse',
            'isGuidedSearch': 'true'
        }

        response = requests.get(endpoint, params=params, headers=headers)
        data = response.json()
        provider_info_responses = data['providersResponse']['readProvidersResponse']['providerInfoResponses']
        print(provider_info_responses)
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