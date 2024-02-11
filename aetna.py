import requests

def get_data(zipcode, plan):
    #https://healthy.kaiserpermanente.org/colorado/doctors-locations#/facility-results?zipcode=80401&keyword=Urgent%20Care
    #"search"
    try:
        import requests
        import json

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
            'searchText': 'Urgent%20Care',
            'distance': '50',
            'productIdentifier': '~MPPO',
            'state': 'CO',
            'listFieldSelections': 'acceptedVersion_wjtk0,affiliations',
            'postalCode': zipcode,
            'pipeName': plan,
            'siteId': 'dse',
            'isGuidedSearch': 'true'
        }

        response = requests.get(endpoint, headers=headers,params=params )
        data = response.json()
        provider_info_responses = data['providersResponse']['readProvidersResponse']['providerInfoResponses']
        
        urgent_cares = []


        for entry in provider_info_responses:
            location = {}
            location["fullName"] = entry["providerInformation"]["providerDisplayName"]["full"]
            location["address"] = {
                "line1": entry["providerLocations"]["address"]["streetLine1"],
                "city": entry["providerLocations"]["address"]["city"],
                "state": entry["providerLocations"]["address"]["state"],
                "zip": entry["providerLocations"]["address"]["postalCode"]
            }
            location["phone"] = entry["providerLocations"]["contacts"]["phonesVoice"]["number"]
            location["latitude"] = entry["providerLocations"]["address"]["latitude"]
            location["longitude"] = entry["providerLocations"]["address"]["longitude"]
            urgent_cares.append(location)

        return urgent_cares
    except:
        return 0
    



if __name__  == "__main__":
    get_data(80401, 'Open Choice PPO')



