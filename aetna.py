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
            'distance': '25',
            'productIdentifier': '~MPPO',
            'state': 'CO',
            'listFieldSelections': 'acceptedVersion_wjtk0,affiliations',
            'postalCode': zipcode,
            'pipeName': 'Open Choice PPO',
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

        print(urgent_cares)
        return urgent_cares
    except:
        return 0
    



if __name__  == "__main__":
    get_data(80401, "Choice PPO")

data = '''
[{'fullName': 'Hawk United, PLLC', 'address': {'line1': '495 Mount Vernon Circle', 'city': 'Golden', 'state': 'CO', 'zip': '80401'}, 'phone': '2145075317', 'latitude': '39.708539', 'longitude': '-105.253828'}, {'fullName': 'Solis, Janaleen, MC', 'address': {'line1': '495 Mount Vernon Circle', 'city': 'Golden', 'state': 'CO', 'zip': '80401'}, 'phone': '2145075317', 'latitude': '39.708539', 'longitude': '-105.253828'}, {'fullName': 'Patel, Sonal S., MD', 'address': {'line1': '570 Eagle Nest Court', 'city': 'Golden', 'state': 'CO', 'zip': '80401'}, 'phone': '3037483800', 'latitude': '39.725883', 'longitude': '-105.217576'}, {'fullName': 'Colorado Pain', 'address': {'line1': '755 Heritage Road', 'city': 'Golden', 'state': 'CO', 'zip': '80401'}, 'phone': '3032770700', 'latitude': '39.727304', 'longitude': '-105.210028'}, {'fullName': 'Gold, Dale C., MD', 'address': {'line1': '750 Warner Drive', 'city': 'Golden', 'state': 'CO', 'zip': '80401'}, 'phone': '3039254340', 'latitude': '39.728334', 'longitude': '-105.210705'}, {'fullName': 'Vollmer, Jeremy C., DO', 'address': {'line1': '750 Warner Drive', 'city': 'Golden', 'state': 'CO', 'zip': '80401'}, 'phone': '3039254340', 'latitude': '39.728334', 'longitude': '-105.210705'}, {'fullName': 'CHPG Golden Primary Care', 'address': {'line1': '750 Warner Drive', 'city': 'Golden', 'state': 'CO', 'zip': '80401'}, 'phone': '8009530104', 'latitude': '39.728334', 'longitude': '-105.210705'}, {'fullName': 'Mahoney, Drew, MD', 'address': {'line1': '750 Warner Drive', 'city': 'Golden', 'state': 'CO', 'zip': '80401'}, 'phone': '3039254340', 'latitude': '39.728334', 'longitude': '-105.210705'}, {'fullName': 'Pickle, Madelyn Elizabeth, DO', 'address': {'line1': '750 Warner Drive', 'city': 'Golden', 'state': 'CO', 'zip': '80401'}, 'phone': '3039254340', 'latitude': '39.728334', 'longitude': '-105.210705'}, {'fullName': 'Holista, LLC', 'address': {'line1': '750 Warner Drive', 'city': 'Golden', 'state': 'CO', 'zip': '80401'}, 'phone': '7202773910', 'latitude': '39.728334', 'longitude': '-105.210705'}, {'fullName': 'Piette, Mcinally Wells Qua, NP', 'address': {'line1': '750 Warner Drive', 'city': 'Golden', 'state': 'CO', 'zip': '80401'}, 'phone': '3039254340', 'latitude': '39.728334', 'longitude': '-105.210705'}, {'fullName': 'Davidson, Paul Michael, MD', 'address': {'line1': '750 Warner Drive', 'city': 'Golden', 'state': 'CO', 'zip': '80401'}, 'phone': '3034934443', 'latitude': '39.728334', 'longitude': '-105.210705'}, {'fullName': 'Golden Emergency and Urgent Care Center', 'address': {'line1': '760 Warner Drive', 'city': 'Golden', 'state': 'CO', 'zip': '80401'}, 'phone': '3039254360', 'latitude': '39.728334', 'longitude': '-105.210705'}, {'fullName': 'Scroggin, Susan D., MSW', 'address': {'line1': '750 Warner Drive', 'city': 'Golden', 'state': 'CO', 'zip': '80401'}, 'phone': '3039254340', 'latitude': '39.728334', 'longitude': '-105.210705'}, {'fullName': 'Johnson, Julianne, FNP', 'address': {'line1': '750 Warner Drive', 'city': 'Golden', 'state': 'CO', 'zip': '80401'}, 'phone': '3039254340', 'latitude': '39.728334', 'longitude': '-105.210705'}, {'fullName': 'Cook, Christelle Roseleah, MA', 'address': {'line1': '750 Warner Drive', 'city': 'Golden', 'state': 'CO', 'zip': '80401'}, 'phone': '3039254340', 'latitude': '39.728334', 'longitude': '-105.210705'}, {'fullName': 'Radiology Imaging Associates', 'address': {'line1': '660 Golden Ridge Road', 'city': 'Golden', 'state': 'CO', 'zip': '80401'}, 'phone': '3032331223', 'latitude': '39.727277', 'longitude': '-105.206867'}, {'fullName': 'Brinkman, Chad B., DPT', 'address': {'line1': '660 Golden Ridge Road', 'city': 'Golden', 'state': 'CO', 'zip': '80401'}, 'phone': '3032752190', 'latitude': '39.727277', 'longitude': '-105.206867'}, {'fullName': 'Brown, Wellsley Montgomery, DPT', 'address': {'line1': '660 Golden Ridge Road', 'city': 'Golden', 'state': 'CO', 'zip': '80401'}, 'phone': '3032752190', 'latitude': '39.727277', 'longitude': '-105.206867'}, {'fullName': 'Johnson, James T., MD', 'address': {'line1': '660 Golden Ridge Road', 'city': 'Golden', 'state': 'CO', 'zip': '80401'}, 'phone': '3032331223', 'latitude': '39.727277', 'longitude': '-105.206867'}, {'fullName': 'Hooper, Nyita Maze, DPT', 'address': {'line1': '660 Golden Ridge Road', 'city': 'Golden', 'state': 'CO', 'zip': '80401'}, 'phone': '7204976616', 'latitude': '39.727277', 'longitude': '-105.206867'}, {'fullName': 'Parker, Joshua Keith, MPAS', 'address': {'line1': '660 Golden Ridge Road', 'city': 'Golden', 'state': 'CO', 'zip': '80401'}, 'phone': '3032331223', 'latitude': '39.727277', 'longitude': '-105.206867'}, {'fullName': 'Wood, Elizabeth Ann Marie, DPT', 'address': {'line1': '660 Golden Ridge Road', 'city': 'Golden', 'state': 'CO', 'zip': '80401'}, 'phone': '3032752190', 'latitude': '39.727277', 'longitude': '-105.206867'}, {'fullName': 'Condon, Lisa M., MS', 'address': {'line1': '660 Golden Ridge Road', 'city': 'Golden', 'state': 'CO', 'zip': '80401'}, 'phone': '3032752190', 'latitude': '39.727277', 'longitude': '-105.206867'}, {'fullName': 'Agarwala, Amit O., MD', 'address': {'line1': '660 Golden Ridge Road', 'city': 'Golden', 'state': 'CO', 'zip': '80401'}, 'phone': '3032331223', 'latitude': '39.727277', 'longitude': '-105.206867'}]
'''


