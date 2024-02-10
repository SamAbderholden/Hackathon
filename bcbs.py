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
        "radius": 25,
        "searchCategory": "ORG_SUBTYPE",
        "searchType": "SYNONYM_ORGANIZATION"
    }
    headers = {
        "Cookie": "_gid=GA1.2.2004569358.1707538625; trace-session-id=b018ccb4-d289-4d0b-872f-dc543ef29792; tealiumid=018d913bc7180020f926578fdfe80506f0090067009e3; visit_num=1; _ga_7ENW64XR36=GS1.1.1707584273.2.0.1707584276.0.0.0; _ga_D114P5TR4V=GS1.1.1707584273.2.0.1707584276.0.0.0; SESSION=OGM1MmRmODItNGYxZi00ZjI4LTliMDYtYmYxZjY1MjY1YTU0; prev_page_ppv=75; _ga=GA1.1.1165648292.1707538625; _4c_=%7B%22_4c_s_%22%3A%22fVRRb6Q2EP4rJ6ryFBbbYDCReEj22nQfbjdqElXpy8rY3sUKwdSYcLlo%2F3vHLJvkkqq8YH%2FzzeeZ8YxfgrFWbXCOc5RTlqYkRzg5Cx7Ucx%2BcvwRWS%2F97Cs4DiijDBcZRQamIUsllxLGiUcqKnImE7Somg7Pgu9fCNMFplmBM6eEsEN2s8RIIIxVo4WKB0wWLdj14uB%2BARClBsO6skYNwW%2Ffced6oqi%2B9fACDVE9aqO2opau9AEXpG1orva%2BdhxFKPNxZv1lQWI%2B6lWb86Dijr44szwCtrBl75X2XtTWP6gsmGGADpQj%2Bmjx8vFbtlLUTrXau68%2FjeBzHRSWqfiHMYwyUXjsf%2FgmaESjqDEaQ55OWoAEpT8WFRWMEb7wb3MdZMNjm3QEn%2FtspvOvibqgaLeJfYtOqWGj3XIa9406VYWdg0Syh2mUozNA6Czbd9gPEPaGXy8ubi%2B0qrCxv5Ruy%2FvrH7yFvuppfQ5r6exn6A2EzXctKxr3iVtTxe8r19SbUPVAejdOmvZkYpbODCiHj8s7uVet%2BJZSgJbcq9Gl6XnllGqlab1gerZvpx1CKcNjxvSpx%2BM%2Bg7GcJy6Ue%2BpLQ8BjOEnLeGyBu%2Frza3txd3t5f%2FzabbqGRypv79WZ9%2F20L5ov16u%2BL29VmDSVWrS99Z33bXl1s71ZffYPgjGYpIwVZTDORsIz427m1er9X9ptytYGZgD0E4fPgje84GCHoxh0fGue3vqdEw%2FteC6n6B2e64DDPBsqzHDFCEU6h9x3cMstS5L%2FDsRmmUaHv2TlJYC4%2Fs4%2F9Gqn2f9zwZ7cnfZppXDBR7KpdhFPEopQSFjGEVJTRhOAdpSmpquBVkrIME4pzOktidlKEzE%2BSAiEmEeURoiqLMFYiKjhKIkRSwgVO0HFEf46y%2BI%2FkfEmPkm91PT0uGUpIkkw03bmZNz9hYElR8YELiOeeFPlHraPdjq9SswGyzX6meuRwOPwL%22%7D; utag_main=v_id:018d913bc7180020f926578fdfe80506f0090067009e3$_sn:2$_se:33$_ss:0$_st:1707586232764$_ga:1165648292.1707538625$ses_id:1707584277823%3Bexp-session$_pn:3%3Bexp-session; _ga_V89DNZFP5J=GS1.1.1707584278.2.1.1707584432.0.0.0"
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

