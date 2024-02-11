import requests

def get_data(plan, location):
    payload = {
        "guid": "65461f76-dffa-4be1-9f64-8049edba3d5b",
        "languageCode": "EN",
        "alphaPrefix": plan,
        "isPromotionSearch": True,
        "key": "Urgent Care",
        "location": location,
        "query": "Urgent Care",
        "radius": 50,
        "searchCategory": "ORG_SUBTYPE",
        "searchType": "SYNONYM_ORGANIZATION"
    }
    headers = {
        "Cookie": "_gid=GA1.2.2004569358.1707538625; trace-session-id=b018ccb4-d289-4d0b-872f-dc543ef29792; tealiumid=018d913bc7180020f926578fdfe80506f0090067009e3; visit_num=1; prev_page_ppv=75; _gat_gtag_UA_3312038_1=1; _gat_UA-3312038-1=1; _ga_7ENW64XR36=GS1.1.1707669102.3.0.1707669105.0.0.0; _ga_D114P5TR4V=GS1.1.1707669102.3.0.1707669105.0.0.0; SESSION=MTRhYjE2YWQtMzY1My00M2I4LTk5NWQtMzVjMDkxYTU3Zjcy; _ga=GA1.1.1165648292.1707538625; _4c_=%7B%22_4c_s_%22%3A%22fVRtb5swEP4rFdP4FIINmJdIfEjTrcuHJdGSauq%2BRI7tBKsUM2NKuyr%2FfWeSNH2ZhoSwn3vu8d35jmenK0TljHCCkjjOMA6yIBo4d%2BKpcUbPjpbcfh6ckUMQSTEQvIwQ5kWcco9iQbwozZKUhel2k3Jn4DxaLUxCHMUhxoTsBw6rjxrPDlNcgBbOhjgapt62AQ%2FzBxAvChCsa614y8zaPNWW14nNRcPvwMDFg2Ri3UluCitAUHRGCyF3hbEwQqGFa203QwLrTlZcde8dj%2BiLY5rEgG606hphfSeFVvfiAgcYYAWlcH72HjZeLbZC655WGFM3I9%2Fvum64YZtmyNS9D5RGGhv%2BCToiUNQj6EGeD5KDBqTcFxcWpWK0tG5wHwOn1eWrA0788ym0rv263ZSS%2BZ98VQmfSfOUu42hRuRurWBRTqDauctUWxkNNlk1LcTdo5eTy%2BV4PXU3mlb8jMyuvn11aVkXdAFpysfctQfCpr%2BWKfcbQTUr%2FNeUxWLuygYo98pIVS17Rm50K1zIOL%2FRO1GZzwEJ0IRq4do0LS%2B%2FViUXlTVMDtZ5%2F0lRhLBb053Isfu7FfqjhKZctk0eEPcQzgRy3ikgzn9cr5c3l6vbxZejaQWNlC9vZ%2FPZ7fc1mMez6a%2FxajqfQYlFZUtfa9u21%2BP1zfTKNgiOSRylMAZDOxMkTOPA3s5Ky91O6O%2FCFApmAvYQhM2DlrbjYISgG7e0LY3d2p5iJW0aybho7oyqnf1xNlCSEEIwyoIQet%2FALadxhOyzPzRDPyrkhR3DG4RBgj6yD%2F3qieo%2FbvijG8R5GmqGUMoRoR4iIvYwFszLKAo9FEQBZThEh4F6q5n9IxRbgIPkuQqnX0GMwiAMe5qszZHXFzeNwBKh7B0XEMs9KdL3Wge77l6kjgaCk%2Fgt1SL7%2Ff4v%22%7D; utag_main=v_id:018d913bc7180020f926578fdfe80506f0090067009e3$_sn:3$_se:12$_ss:0$_st:1707670929747$_ga:1165648292.1707538625$ses_id:1707669107069%3Bexp-session$_pn:1%3Bexp-session; _ga_V89DNZFP5J=GS1.1.1707669110.3.1.1707669129.0.0.0"
    }
    r = requests.post('https://provider.bcbs.com/healthsparq/public/service/v4/search', json=payload, headers=headers)

    data = r.json()
    providers_dict_list = []
    for provider in data["providerResults"]:
        provider_info = {
            "fullName": provider["provider"]["fullName"],
            "address": {
                "line1": provider["location"]["address"]["line1"],
                "city": provider["location"]["address"]["city"],
                "state": provider["location"]["address"]["state"],
                "zip": provider["location"]["address"]["zip"],
            },
            "latitude": provider["location"]["latitude"],
            "longitude": provider["location"]["longitude"],
            "phone": provider["location"]["phone"]
        }
        providers_dict_list.append(provider_info)
    print(providers_dict_list)
    return providers_dict_list

