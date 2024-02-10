import requests

def get_data(plan, location):
    #https://www.anthem.com/ca/find-care/
    #"specialty"
    payload = {"alphaPrefix":"902","isFuturePlan":"False","locale":"en_US","location":{"distance":"20","postalCode":location},"memberCriteria":{},"networks":["NC1M","PAM2","OR4M","NYNWTKPPO101","MO3M","VANWTKPPO101","PA8M","BVV","CONWTKPPO101","CTNWTKPPO101","BLCENTPPO101","BVV","TN1M","NYM3","AL1M","VTM1","HI4M","AZ3M","NEM1","WV1M","ND2M","KS1M","RI2M","NHNWTKPPO101","MN7M","MS1M","MT1M","ID5M","SC2M","NVNWTKPPO101","LAM1","PA9M","AR2M","SD2M","DC1M","NY8M","UT1M","TX3M","IAM1","PR1M","OK3M","CANTWKPPOGRS","NM2M","IL1M","PAM0","DE1M","NYM6","NJ3M","MENWTKPPO101","FL7M","MI5M","GANWTKPPO101","FL5M","MA4M","WA6M","ID4M"],"outputFlags":{"includeTaxonomy":True,"includeVisibilityRules":True,"improveSearchCriteria":True,"includeDisclaimerRules":True,"includeReviewRatings":True,"imposeAddressConsolidation":True,"includeSpfInfo":False,"includeProviderNetworks":False,"includePrimeGroupSearch":True,"includeAllNetworks":False},"pageNumber":1,"pageSize":20,"plan":{"category":"MCRGR","stateCode":"CO","plans":[{"identifier":"8ED0C561D312F745917EED553FDA5552","isNationalPlan":True}]},"searchCriteria":{"miscFilter":{"patientPopulationList":[],"medicaid":False,"smartSearchRequestId":"99b91358-7a7d-4411-9065-15a8b50fd8a0","recognition":{"blueCarePrimePreferredSpecialistOnly":False,"bluePrecision":False,"patientCenteredCare":False,"centerOfExcellenceOnly":False,"sosOnly":False,"ecpProvider":False,"hasCcare":False,"mspOnly":False,"nyOASASOnly":False,"nyOMHOnly":False,"providerOfDistinctionOnly":False,"upswingOnly":False,"valueBasedProviderOnly":False,"lwrCpyPcpRcgn":False,"blueDistinctionCodes":[]}},"demographicFilter":{"anp":False,"ableToServeAsPcp":False,"aoeCodes":[],"boardCertification":False,"genderCodes":[],"levelOfCareCodes":[],"specialtyCategoryCodes":["237"],"taxonomyCodes":[],"typeCodes":["U"],"visionSvcCodes":[],"scheduleAptmntAvailable":False,"includeVirtualProviders":False,"ofcSrvcCodes":[],"coverageTypeCode":""},"rxFilter":{},"brandCode":"ABC","isInitialSearch":False}}
    endpoint = "https://findcare.anthem.com/precare/api/search/public/v1/specialty"
    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2Vybm0iOiI2YzFiMjZjNmNjZGNiYmJkYTBhMTNhMzM5NzQyZmMwMWY1ZGI4NzAxNzZmN2E3NzkyYTBiMTkxMjA5MDdlYTczIiwidGhyZWF0VHlwZSI6IjgxMTBkZjcwZWExZGYyN2I0OWRiOGM2YzZmNzEwMzYxNzNkYzQ0NDhkZTE4MDRkNTgwMTBlODQ1N2E2ZTY3MTAiLCJhdXRoSW5kIjoiZTcxZmY4YjBkZjU4NGRhMDcxNjA0YTM0NWQ5ZGIwMzBiZWVlMjkzNmU0ZjI1M2RlNGVhYzAyMjRmODMyYmIxNyIsImlhdCI6MTcwNzU5NTY4MCwiZXhwIjoxNzA3NTk5MjgwLCJpc3MiOiJQRl9QVUJMSUMiLCJzdWIiOiJqd3RfdG9rZW4iLCJqdGkiOiI1NmRjYTlkMC0zMTJmLWQxNjQtZTNjZi1mZDk0ZWUyNWViYWQifQ.ef64UmPFIBTY0lmKEQ-JxrNKVbDKStvU0fHjaTS3vjY",
               "Cookie": "AKA_A2=A; ak_bmsc=0C4E7DE4A23121BD71390116A0C9B030~000000000000000000000000000000~YAAQsVkhFwZaPWmNAQAAFfShlBaS5Vwqsq9H2V01AKzkJlStMgIFf0H7H7sThiE6Cb5DpgdHrloWG58ukVOCVhwQZuiogDRkNeM8PttahOxyivOoEhMFXNfkPLhyVyrHwc+gviIKD5x18T5etpPyf3JyUwJicSXzTSkcvp+vnMEi63mxUBf0rrqOseyzzFMSMblKVcInS2r2B0gkYUBdJxM1Ng47HcQT9upxJgY4Zh7lz6j1808Fgqd3vfqHsj6kBBa8gfoYzVVXuyxoDUKD0k0Xgk55eHMn1IzPSs6qGmvEC/UOmkFaBFG6egt0u7Rwc3MONV2xEbj0hYWEmW39wV5SmzAbyJR7TwTzrjL0z3nV5LH99tfHhhCxobriMGYfrgWVn/b2XrF2oQ==; bm_sz=FF1C0C6AD68F0B4879A591A018886185~YAAQsVkhFwhaPWmNAQAAFfShlBasAS89qXnmPNFJvv9oGVOYXZLFzvBUTdqgJ7R5xUiCknLrepx9v1MyswmdVWfFHIVFmdHjm8fC2X0qi0q+XoVcknd5tFDBA+qlCUfVSgceieS3Aq5c8+g4A5WPU41GaDo6r5SSMBwxj/ZmsRGfa/EmBz2yuoEfN9Vp/1BxGH4vu1wGIFPOrcJZparXZpmmUdQAMLoG97b17p70FsMNimvUfBrsGCbVHWci95nEnAPClU5URGwt6DJTytE/C7ixlVa4cR8zjBDZT/vEN7AtPogkWj5lJcxvs+sTr0DFWk/KIp1YH8QLBqjRHA==~3485748~4272435; AMCVS_95CF659E533DE4C90A490D4D%40AdobeOrg=1; TLTSID=56dca9d0-312f-d164-e3cf-fd94ee25ebad; _abck=E13CE833B2D5917D92E189017A8EC8AD~0~YAAQsVkhF8haPWmNAQAA2PehlAv8ltI9Rp/7tZA9ptyR943MIJRz1NEzq0UeKR4O0pKJreYnkndbF/qxkGBm0Bt+BrJBZkRbTykoaMi6EnhdwGkzh8ff2ImO9sGmwwUoLX1nlj6/EIgXkXkQPwyzIkteUMabXwhmLg4Z3jfz+KdZ8nUhmmK/Dd3OSfp7hEIyxd/pTSsN5i1t+jvD2WIuBtFHsstuLiXs3J+MYiQnVJKYoVr1Q25J/GcI14bhu7+wcM5Mjr8pU7TPJxrbeisY43Zxv25w7tsYvaZD9NcQUaMNgRhHKyah6snqstB88SgNepdTzsm7wu8WlCX+iva/4Nlxd2AKiFs8fK0K+UcKMTzkD55WMO7PRafB374tzXfM6puIyUDjgsaSCtLhc4rVVpRLUWrZWK7K~-1~-1~-1; _dd_s=rum=2&id=6f60c9b9-8fac-4c69-8010-19e0df5b5d70&created=1707595658034&expire=1707596558034&lock=f8b4d48c-983e-46db-aede-07311b697050; JSESSIONID=sdaUof8yEcs4UGxHqGG5SNZW0x6hbaABhAnifjleJoq6EucR7mqK!218188681; bm_mi=B5C675FC958AAEA70ABB58321540EEC1~YAAQsVkhF1BpPWmNAQAAPUeilBYJeVPUmVJb4IWTYiZuDE6kJoECGNxiwnG5KEMNFxonujKUIEWCALzatCNcqHE6fMyYMCtVs36Wi6rPPdOyRDOlagQJKBGMUiMINHplN81IElWEPF/LgYdn1nJjvCCQOQO5UcWoBzxu4g7iGHVj6oNXVvVs7w7NKEKe5C/KK80Y+DsLeehsE9ZFU/RKMXQVNZsZqoOyM9E5ALcJEcskhMDLH9Upy1RJShE8oe0zUAKcW2467wsHcyGeH9rE2XLffE4ny0d+dJnb1rwKrAOmuA0qkH5UPd5a05Thmiik3J+jGRDLtNqhzQ==~1; PIM-SESSION-ID=QI0RKZW6VJgGMZPo; AMCV_95CF659E533DE4C90A490D4D%40AdobeOrg=179643557%7CMCIDTS%7C19764%7CMCMID%7C41875618049070697191703744184882563782%7CMCAID%7CNONE%7CMCOPTOUT-1707602878s%7CNONE%7CvVersion%7C5.5.0; AWSALB=8GkFAcRIelr0j2TsqzL8bUT1q4ES/KcepXH9WIaKeP5ZvXLKJQ/QVj/ZiHZYnqH1bA2KvlGHXoXm8nCm5Nss3fLtbgCWb3gBMYg+f1iZ6TEQuHAqeUgOnLBVep8y; AWSALBCORS=8GkFAcRIelr0j2TsqzL8bUT1q4ES/KcepXH9WIaKeP5ZvXLKJQ/QVj/ZiHZYnqH1bA2KvlGHXoXm8nCm5Nss3fLtbgCWb3gBMYg+f1iZ6TEQuHAqeUgOnLBVep8y; bm_sv=482602009EE1B73618219B18452061DF~YAAQQo0hFwJXbX+NAQAAnnSjlBYnbGzKmnlaWivEtd9auCd3O7Kfc5yvaV/1lhPV6f86IEoT5ZnJRo7i+H1lgVWFdlmQ7hBBbH7bK+2zUmhEFe4Jub6nwjS0MljTkxYPhn6dd81HSkVKgNmrSjfQWKQAWfcjnINa5UFcYHkvcLsy6YsCetbAWVIFwTKzIL2KBBVcVJ+tUd49UVNloRxfDIfmT3g5xNfmGcJt+H/OHnuCyrfyS/xO97ym7+myRVS81g==~1"}
    response = requests.post(endpoint, json=payload, headers=headers)
    print(response.json())

if __name__ == "__main__":
    get_data("PPO", "80401")