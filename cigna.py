import requests



def get_data(zipcode, plan):
    url = "https://p-hcpdirectory-waf.hcpdirectory.cigna.com/public/directory-provider/v1/providers"

    headers = {"X-C1agk3na-A":"AG-YOLNRJQ0wopNrkkiih1VQkE4iwLpxkPnAy7wBVmPGjqP44I1XoLKBJfw8qG8RHRziB_mMI-lkQ0NdWA=RYOwiaKusSL1klhL-Twg_9CX9rANoX11255uybkdNFRhkBTFpeQbzppqAdtIIGgb871GYmPBHx3BxiXh5gK0ybzD=pmADS0M5Ayr5v3ys9HJZO-O_mOY4RCq52TwW81I1QNXYiIObixdsgTG4HCgRJ1Ry5XD1RfdYPnfdVpeA3qkgU8ilONFEPNFSFfHpwmonBvpErxiMfvjnTmjSqZjjK5oNGEYZvJHmRimEwS_NdiwEb6RlC5y=jJ2LLfQqLP6zXYJDi7XGzwirpR0oy3nx6Nb9WSpWY=Wv4dwr73KlusYu8LMwtGMdFV06YXFJ84CK-Ulmxv7v4Zkvb3x6k8zQiA9CNgDZRTtd0nZ3OyNSmm0Bl6Y05IjbgIT3EqRBJyxSZ6tlK8U9UXBh17pRdPoF4Yn8nd_aDibwDGJVMmHYNo1vd0JwhB5VBHnjDfFBXNfYuTKVj89q_x-6uqjwa9dvFTjSBQJPP4T=iRpWO3bDW_YDtYePOFIFo2fEIIICb-0OYQ3A4FNR5yNLa_V5-drGz2OrT3nNtsqXwEOn293XFU9xHgnu-kdrCXOjqwN1lEC_RDY7Jf8rZPeMr1na3v3-m-Rti2Y1ywGzRdJ8ni_FdJZELdps-Dy=MXKi05pfFYAE1H2K9eU_p16e0hlLhUPxOMKiGU9CiT20378BVqiMyJTa8CGiz9ug_0iqPLJ2lrOz83foQo3UQWbwl3YJ5TlmGe1U93DCLuwsIiVDdlOxeZP7hA=EsamrfDOmWI=pUtaS6gbWdb12uppuHkRlRs_WCEE3bbNZmnllPoFZ4g9iy_vgTt4HR0urBfJxSrJMOAsf3IrKwRYWH4RlDdSAUgDrkj_xtnI14h6vUhGAT6NDpeRGsVbj64LRL-0gXz5rPvapmapbauUI_nzGEAgAKyqj_9pQ0bRsUyEtJF=9PHj87GVXMiZX=NdO8XayGE8UShBt1wmoy1xtR_546TfxL0OUhwUIXhrR29PjVk_-b62FM8ovmdaOrgh3uxPkrYA9W-jDIWTsmroM0Nx-lA5VH_xfIyXW2=n4dxFSdvJXaJihCUNH6CTf3m69-92TrJoKsuSnyaCLpsyeagP__=8OsgZsX_dggyxMVmHHNML2SL7JiCYl5R6ogPz36QosDVe9b-K6YQ9K1O7RVYmeU6QwpE8Dp2OE6332RtwCQKIpKHX4j8JA9gnAqtgBfKMTemSVF78M_RtZZGFbvzj=MfrWAYY7nIyfVh61nEskYkltA3jz-=IHAjE3glR=Pfq990m8jFaKOUfGsFxGjgTXv7ppiR0Exa4r26tfsYrknkad-D29ZfNMeIUf=4OmtFVDaP4=wrGuoIDqNrhOQYU8pqF6-TMn8nXoK-Q2S-wEa6uz1kbL0Gz6VqV46mXXPYmk31j43LxzLi8stWSGk8RH25ZmkmyCwd1fCZkVrPnlyFPYTtKb-H4yUU7=zXW5vvVzVMfwIvtIMhT82zxYZkdlyVKLlNCTxiozza7_FSoTXmmuyiqgz=-wwrYaW4xWTICWbKIj86ys=nfKTaOGCPH-7v-iqF7kZCdDr55C4QttIeLwI3s1BShSo63SZj-8HW8-hfF4Fhj-Auw3_z85TZ=aP9N5C2qVmjDvDCxps9LV_t2_2qt9pwO1A2L80ek0ZaXx-KNW1gjG7orXJodCF5iQXzfUdDRJeL61VShYA8UTgM3vexreXyhG2M8kJC51TdIszSlGZOxI78xEMLQgivmyfVgbVvs7Aam6yIOu0MnxjCaTS9UkJ61B8jhFDm=bsXVew6OdrjssMJryGn_zRqzux-1iTRD=f7rXjX6shCDWHisANJsfVpUwYuyLBij7gmEl9YhoS515CGrwJq54UD2xsdi3JptAUmvkh1WhkLjwdnAxhw0F8HmRvmDpHMjxaoxgw07rYwe-bRx6WWMa8SqTt4ptHlUryig5KXe09H6AZ3nBPwCWZUiskfifDtoli73X0SluLmtAbOLRY0KTtX7_wU42TC_ifI-fjr3sZG0f_4fQUkOwQln2JrPsbVDSSwKpA02PvBD7A0eYvjE=6QGjUt3dUi74vORzyvoGfzVvv57-oXv1_e0yWyEj=29AwNJ81v=khhBSf5BYP06Rk4AYdKFZ8MCAontizyfOwdP=FB2Txnawk-A5el-YHa28ueh0zwW36ZYi9YWzsM1Y479ur1h1-eEzLziQR7MeyZvTvVUSJtEG=LdNYTwsasEmY9uDj=sJo0WGDfLNsPx-G6bvq9Cq-xiXRhYFJZGHu8Lop9ZHSI7fjE9ADVs3EB0RvB0hjGTLeHpCt9NFM1bZff70sY4uqPR1D-rIBb2FphTS_zaM6TGpvW7pZuYrb5VzhQSnSYPLUnz8ngGMElGhC95VbD4u=WmMOI=N144XRqfxxJY7brA0LCLn=KqDyQg=Z=IDga=Rhgu4wz7RytYC-gHoFSDwlosSEUyA7oPRyBQ7w2qRhqpA-fybWoiVZICIsDYuTaKnZNYwXaL60=YHL6bDeNFfpKWQKqqTh7TEW24FG1tsfYm4W5wb055y5AWx3LC1WmxMPQWei-1PYPXKe-5_uG=F3ussyMEtK9st3vX_Zq3gLl_-fKoGM8sXMuI_gTojoq0UXeXMZpCt0WqqFlavau3tFfNF3ba=OD1VLzF2BWMqmH3WYPHZGrZNRHLB=Jh0HDf2ZTf8D-hn7IKeI02PS5JgkjS8Sktuts7kBxqD8SkxrQ59LEBx6q0PUCWJ-aP=MXLoQPMdZwPuLl4RI9GmVkRf0V0Tku7KgYekJ9WN6a7wztQWyX8VSXQVbIEvR2Z4fKfo8qIWTodjBzVeB-0vNIixsJoHjrO2W6G29o6RLitLpxiPFd-Jljau5i3U76OerOJfU6oELEkLGPEnae9w6AYIh2=Ak0-IDqh=28ZG93Pma6995dAIBHf1Ipkam8sgn9JMYoAn6swgBN49KztnsZ0vV8F40lP4iKTHPRJmDAYqDPXff8ahVDKAhfutnKyyxYH1ug4z4eVKvMa1o_FKQibupDsdnQmbIjn-1NOnabipHCTfygz67gPiqVlNpugbgX_mO2ooC8WfdxiHRp77wmI=vgvnhvjaldmbU41Skezgy-FKWtm06ka6ofDV1tR-IDB-2wbebaMQWJuNHK0xiSGid-hHeX-wINYhivH_IXwe-jt2zB1BWzPmzFzhJnstO4hJ4BKzx5D2YurjBIL=sQyu-b9nE6VJlGWuO2iMvLfSipx_w4bv=0U4k7vZQFYDK7jtToeeY_KJiHgYWeyvqRefDdhtMXjaRqYlU4UyUz-GRgqB_6OpXxBJGpnsvomFMp5g7Q7UPl059hQaalogR20zuXgHrVj2b3gZqW1prVsSppFlEre9khqLgn6PETK6le4T_nCeaTiGxlsw3fhTVHtjXo6AGNSlhehyq2SVU4_f7Evapih6d8UlD12Mre1fLmxzhRokqWtf7FtOdv1sfqEj8604NR689To_jL9XVJzgZ9S8RHzqFaraePdFHA9w=grahJmA-7Uevt5OPagzEWZvLsYm0iSVTqN6pgdAKuqNxyvwzKQoZ5t-kzMnOkzI_KXERKdOb2RtDJNAfJ1CuDeJmQt=BDmSwY6FroLfZ_GXR=JexSbSpfDJsqOzTw_t2pl-QXWhqBsa3tZvXVLaaVDLNuC4HJWCJkG_mT7bWAJ6=DDQ8BRZ3FXgBRqgpzeiKf3LVq6OMpMwo_aMhrkK=fo41Ul_AVe0utz3Kgi8MO7-UKDtjD7n1l8Uv7AIznlJi9878ywIlWt2Dtv8p-Dkdhl=blNGKDddJWEbHPqvQ9-lk7MkATxADUu79whRjkY=h5Jji3HbZjmPgFAreG7lyKiEOWkus8Cx9WEwK-heAEzb097uWI9r6nnWZwt5uy9Vv3-ImT60hagWPIHwj6CU-rfah2hv0qORhbPvYzF9wfj_egME=4BmlOxs3yLddgpzBVYhodhS7FDeeyLQnUmB8q37lYoxSk-5h3kRhnj7GBCDgjn1i=TPGmA280WiHETG5tsPrYFy4HRQS9xRJVBZT2-MHNzGwgv66drz3UBzvbME-G62Wkb8fVlzu0BfgRGp0ZMXab1ga5saHkUZBL666m5ICINP_6WY7AOdYttLs7MyTEBMe0jet-ox6U5yCTNAS-By1Kz=bQAjEk07RUM2bAk-QUCoB_vakXKptdMKR2jhtqqkJDM2VyCHetsiXiuSKw8WlgAHBf17BwehgfXSf7GArYCXNySV8a=qkz3osXG9Gx0VnmvGnMwyu-HufMLeCr=mAeWDD4OyuIfrd9GHod0uyxtN0HBZwV6S2ul5JKLfJYehy1QHDtQXSwpybJ3GTM5R6=Q4eZufiylqJlL4QyFVo=EpbMLyHU1EIouR6DQxaCg1aVzorGkIRuC_AzhtO2ZI-xIxKeR0L8BfS73MmWm-TVJTU0nQXHpFeOoIRsejabyX4zgN5gLDVVzk0s1oxzoWIHaXXzGZwlAqNmrr=RT_RghU=oL4I9l9_OSjY2M0L6-COualWhgg67EBPv3XJSmdZyNlu36n7yIILI1txxzLovqZjQCaV2AVRGoZfxNHuqPkzaI-SLvoS7VaOMpa8i-AxrNYHqCy921x1Jvtqben8f_BqM32UMHk9ueUNRVFDYWuqK56pVeQxqarbrsPppE97Gexq04YD6Mvn-MdHq-WxZVWJh_jgnm0Kd98U_4FEu8WSvn1f4U_=MfI1mF==HUDZUVmZZ2rP5CvMYW5u9UOsYEopqxB4hJmC4aXgn3oSRl3T9d4bfH6meDtfhbbRVFMnC3yCJgqbLmyRmVCoKE9SkkLkhtxt5flYJNge_srS3xSbm611EQ5KhuKkZs9klr=6Z2Z3PPisJh5bwJ1O8jFmOvSDUX7CLLHSoby8q0wClFAj1IjRAyWvDxtKosy4Y5Z0_F-RbtaHja7NZzgBpbr6izGgXzbrMZb7y2bu0AAgYteooK2a_8rjNooIgeyS-3Nh=EeU3vMOme-4QUni2IGLjzgZIFXTHFSmNk02VfNaOZ-g5jIgTlYb=Us8j8WR8is0SdR_ApGXMHmzfYZBYbznbCxaLbvNeCPlRqkBS=i2ySogLrVZ1rzNj6KhVubuA2-4Cxr314ad6CXAPGzdrMpSWSzl1vO6jAk0B2RMtJRkXt9b9uzJqzTYA1rykJTuAK=RW-QY2lsNQBjd2Xa-q6YXiumfC=q47PH5nOZPBD8smJZ03xwQVN5A_gY6FU5ClVNdHe7CDIp3UjSaEfpzKZ8vjs_E5khAj6F0ewuXkR7PBsmRoQG0pm8lM8NBuy7Oq4zyFEM4Frbl-4aGLzCAjS7E=A8mGQnmXENzS0-RRJyZwlfjfBnIU=qFW=k5q=HkjE=_PNTHlS=nRAB_PxGLSA-CzH2urYSjne7Ar4VNIBdeqO1vXMJQPQ8CtUK3Ub1BtnfF_-_y0MAVaZJ5owHN327NUQ5PORLbelun80MHz2i=MxqbMA9XVDIzKD0uSP9t-EYZySo5f6RnhG87lxafeslUo3JJEA2dbR563Muju=e8YDrhPCfT0V8DC6swxYIfQElMoTePp_fr=lOpNh9F65OW6hvd9o79qeJ6pmGFNzU876R3xe8U2n9k9kTJyRXQHb=Yff33S5R0AjPsN7CACMMURfxnhxxVbU64QIKEHBULU=9-r7eadPkVmLt-el3y7A-TYK0hxK3XpEl1OrITw=KCmzet=Pz9o1Ti8vQEInCqOHIsR624l4aztqIhCjTMsSaNG4G7s9YG7Cx3LmiznU9jW5gB5dD9HS7En2CG00EEwWd0YGp_dOprFfKVVi2C9sX_nNibp-iDY2uX8mw=60Kzskxdv65N7goF==gjeVpdOw3glz=MmEfjRhVXyw-lXLq2Z5fp=YDbNLSzOamKiKj9UGo2FE-ysgLotaLoFB7rqFNH9oa8uNM7vkYfqWXddNdm3H_g9aiTBm7ouWTaOC8-9HInPRCKTPzBIyOAPJO9nRklyu5f8CBrAItzzVR0ENPyu8_OmV2pAS7rYnBOd7PbFGN8_o2fUt2vMhXzH8smf=ErlrHm4t1HF431DLZbI98rzKBQz-W=7bqKQQTdUjKK0PypPfuyKp6XEYjyqWhmLO14CSYM1IjZ7_vNTQ4hoeQq-FxaekXkgh6nT=AD5UDyfYVHL3jQ1fvR1=BC=YtD=wa7oMorpBao3IRnS2XrbW0XnE0OhF1LmCEqSB44ks=lCKbUqZbB9jM_VNmrufIdkW1ICVQOgWbIVzjiJsoSMOxqNKB_JOVikCaDiaP0lBKdCKSUCIQ9CbnQb=ytp5hTOw994n8EhPh3Ab=KUtyiRBdfx9uG7QhkI3NY2Wm-hDdnTUjz7h0BIlCBX4NA0BtKRGC9gYxWJ=17kxqa5O1=vA4fM4FR9vhLhBiJVzC8FTjmQAdCG6AoMpOWl=FK_jkz7pYFkOfMUQgn4mQaD2h2mVe1Ar_D5_aZzYrHvTtaZzkE=Ag4eCZVHkPolTxLJRxQdaWttsJb1-p8=TrI0PNGGMuPT72wkPB1ECFA_MpmIss31yGq6HYSPgkks7s62AufPEuR_W_Dmu7aXJwDuzj04h=mINeUdWrjVNIixGkV00lWDbod4_7LZrGdr=FORh75BNihwxWv826bFx5B5oOqf53Bpw1N1==u_q=vzGu5nBU=7VPxGd3KKJS4Qg=nTJOK3fy9Us2jJXQAEIjjUMxCz_9voYof8h5jL3IeThVk6aDwUF8AQxmAC45bEIJkwvz9rpw_XzI9ZoG5oLSYm0ZjwdHO5lz5X1dpVIq3ishaUCQs6huI1Ean8b5wv-fDYkbak2UO6JQzMGOxOjkunoIMt_7KOAnHrn5NbykMeZdxLm9YNBdUOOBqiYa6QhSDfzP3Rv5qt0liVL8lFlKPt1p=OrAD3WAza=SFnRKgO2IjFFvhJwx330bS_6G3yEa7PXQrn-VhfYGGDAOsGpevTC762f4ECL6pUVCO-FuiiGXqYYL=HZJMOKHYMie4AEJBbAehKltGb-_0Q5hglBHxb6daWODMKV_xR8LiqNlAKhPAJqvBr42Y=tBWkxWDYofC_ud=q1oWYkRXVvJaAEdNbdGA7D8=hYm92mBrbeXhJ9upMIRaixPrqPEtjXGyyfA_Cm8uIXEVJOvA6gDZvo-V0IFnwtBq_kC02jaQX9ri_X3kIJ8VE_J0o4CW=aROn5SaHV6HgYwRQs2LCi0wEIe7KXSmPRvEKuEKkb7eSnR6XqFM2XVl9GAJzWkpOHUaCdaBG4EMemzN8tdagduD_ECntoVUfrZ8TpAVOLwIyRFOXtHWXLQGOUOy=zHFI3SZbltn-Bd3idsphoCux_0Fph9bA=iVmveJMIuPU-bFloUUSjXUmYbqwKWzCWQaG8DvQaK=k1WPHFF_U2=iktBvjklfEo=4yPHeqIJD=2Puoda8v8jlLgAwC1CWhbNmNsUZK7ERPOWRGaOTydXheIyGUGMkSWv8=mkHOGXYO=mzG6",
            "X-C1agk3na-B": "bfukaj",
            "X-C1agk3na-C": "AKDMX5WNAQAA8ilyjiNnyqPq1NKng6eQvrZ_hoNAj7WFBr73nOHNYqV342ue",
            "X-C1agk3na-D": "ABaAhIDBCKGFgQGAAYIQgISigaIAwBGAzvpCzi_33wfhzWKld-NrngAAAABSQe9sAFxjquurJHxmpAyrHSocJro",
            "X-C1agk3na-F": "A1iwYJWNAQAA9C-WxDu5d4b0D_w5Iw_96CKw6vE9Q_kIMYitQ2ATpYYhU0ZbAUOmNvWuclIDwH8AAEB3AAAAAA==",
            "X-C1agk3na-Z": "q",
            #"Cookie": "aH1sihCg=AwApjZWNAQAAH9wloCxIjF_wztZOXZ-rIlyrTtloPikSyNSwGeu7yr5jsPmbAUOmNvWuclIDwH8AAEB3AAAAAA|1|1|175080ef8ed79949ecd991a4279dc1572b5811f8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            }


    params = params = {
        "consumerCode": "HDC001",
        "searchTerm": "Urgent Care Facility",
        "providerGroupCodes": "O",
        "medicalProductCode": "V2V",
        "medicalMpoCode": "CO002",
        "medicalNpoCode": "CO002",
        "dentalProductCode": "ADP",
        "dentalPlanDescription": "No Plan Selected",
        "pharmacyProductCode": "RX0100",
        "pharmacyNetworkCode": "0100",
        "behavioralProductCode": "MHSR",
        "behavioralNetworkCode": "6",
        "specialtyCode": "UC",
        "zipCode": zipcode,
        "limit": "20",
        "offset": "0",
        "searchCategoryType": "place-of-care",
        "categoryId": "91121",
        "fields": "providers,sortTypes,contextMessages,disclaimerCodes,alertCode",
        "channel": "public"
    }
    # Send the GET request with headers and params
    working = False
    i = 0
    while not working:
        response = requests.get(url, headers=headers, params=params)
        try:
            i += 1
            print(i)
            data = response.json()
            working = True
        except:
            if i > 10:
                return []
            continue
        urgent_cares = data['searchResult']['providerGroups'][0]['providers']
        print(urgent_cares)
        output = []
        for urgent_care in urgent_cares:
            try:
                location = {}
                location["fullName"] = urgent_care["name"]
                location["address"] = {"line1": urgent_care['locations'][0]["streetName"],
                                        "city": urgent_care['locations'][0]["city"],
                                        "state": urgent_care['locations'][0]["stateCode"],
                                        "zip": urgent_care['locations'][0]["zipCode"]
                }
                location["latitude"] = urgent_care['locations'][0]["latitude"]
                location["longitude"] = urgent_care['locations'][0]["longitude"]
                location["phone"] = urgent_care['locations'][0]["phones"][0]
                
                
                if location not in output:
                    print(location)
                    output.append(location)
            except Exception as e:
                print(e)
'''
# Check if the request was successful (status code 200)
if response.status_code == 200:
        # Process the response data here
        data = response.txt()
        soup = BeautifulSoup(response.content, "html.parser")
        print(data)
else:
    print("Request failed with status code:", response.status_code)
'''

if __name__ == "__main__":
    get_data(80401, "Choice PPO")