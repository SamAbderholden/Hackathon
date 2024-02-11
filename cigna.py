import requests



url = "https://p-hcpdirectory-waf.hcpdirectory.cigna.com/public/directory-provider/v1/providers"

headers = {"X-C1agk3na-A":"KVlcKa3BHpNJA3IFuqutvB2z6t97zzJ3G5jCLYItIctfsYmP2JAWJeygy6IqhygpmhtM4_nG5OnxPPN1a_pqmQeYHu1-CGcDmntQZKweh=fH4XxZoHLlf2l2GTVmXp_cejpxEYnh9Q1cCb647NlrDi5hq3=iusr5I=gP0iAq1evpViNFrPKL=-3yOZPej43DSKJdn32HfnyK0CYNzENMu8iX47CGe9_ezN-0=VDWoeeQuyOBTbn9xGlgChXS-f_x5DESmCf-PjUhU8DWi95UGbh1Y=hf=qmc-97ZmdY_lBzbT8fc4Qy4BGcU=g_fpliYPhdKhxzOlvq6sub7pYqaY4OCO6aB74VmSOCoK3shXVYapNOmiWmzQ7WNKScmgDLbNp85E9hfxlzJ9Yc8y0mrzGXdDWheu0eiL9CLK1t=4kYZ7FhHzwqKv6lYLnGPHq9zb5Xanenn8Kam=IV8qKAxX8aKJgFLxhuQS6kwybFTEkm1eMq=PCCbmWYGhTjh=AnqgrEB9Wi7yK6QfpcmOZa-P16Ch8oNL8cwztyt7UEVD-=ZNTzJZT561NJsXs0g52zI55AX5e8TDxYnh3ytJI0THDIo9EJK70NLo3wmCjcjKOdun=f_Zy91sHumgJ86CarfGFHOkdITcL6SigKGleL-A5lbCnkQ5LErJhG6HtVaDs4=XmhQ_Oe-rjgE89ddfTZK7NjaQXr=IKmnOqMGaHG4_aZGHfZEw-BGjOegmk21JQy94Xx8kuCw_D04roaufLn19AJI_GlxclJXmz396KUDa3LQj0=m7nvFNMBencSvqKnbEwbdzEhU9QiWGjYSGGAJvHKi65h=KTBSDJWJ15ENLAuFwOMXsIohmaimH5Sr=qrequr0xhv087XPtyjFsJ60XHA_CGOu4i=_ULVPv5fp8s=Kr-bAMwVPMj=0IPceTFka0nr4B_UHdIzb3efBJiXKvdDPj5OUpcFN2b-96KHfVeomGnMIrCFjUECE-l6ZimzW-AFE23J4t97rCwun94PJYzj=4=1oDE-6vBKXufHPgzrq1zmnT96gYj-jE9q8wrYFBrxJYPuBZjLddJfGjsICxnXJ6CLx08ryiokED2GrtqlNUaDX0YO_fTLF8MheQJ410qDrt-viMmde=VQhKZtwM88Q=bjuIgWFUQvHXz1-L9awGXIYz63vxrjjN3v4oo--GQ70Ouz36YaLSWrUYun19YsiYzG_O1wGZPrDVrnyqyYl6ZbMC6XUXGzwsy-71S23sZ1TEMz5D7kBx5JeDkyHYFd6Eq0-fPqJ9LpGhQkAkJxr8DTaKL4FhqPZsm5XmN9lcfQLAm0DiQ5MOpAx=Kyr8rDtMmTNbshqzV3TP_liGJteVpj4PW6h=fDS8gjJnVmZl_5YZ2ZPM5vCLkk_q-cV3y-OOIEh_Brgp-vKvNQQ3DOyV5==k7K3x6Uz1kLdWOD=bnIjFdZ_mKmoz3n86LOElY7EJtW4xBiHqs2Qlb3p0pS9G8V=tqV=BYpZYhFVjESDqN_NMWsD05yhK3MyInVBHXIyaO0D=j_LfkNgaFsKMftHd9sQD3_i_z9VTDLXLoZdqfdtVfc3jc8AtqJE3-=B2wJSJ3QE2mrJp7K4c9z0EqafGa1-epzdtzfMEn5eT3Jysz=7cZylwgo6yA-eMN0LMgxcUF2EcqX2Luuabdn8Fq-G4H_aLqBD21Hg78PQpBHanBGFomlJaUGGhKjSFcj_K=-2ZzZMnVTZd0P4jNqK2ypp=dnTVBGLgG8ONPQDlU=zfbdkoWoN2UhAnpB762x8Hx68UXwv1hYMpIGecjExiVdXI9yblFabFeBIpVtzXMWyy6EfmOPDlEwkijaWyBS06EQTXDbK7NGNNyi6PF_TNQm9g4DK=P2jz2grW=x2I_WQNVd-FOOJ76CfJ_U2qBmGSGJQW6nJPl0qmGUZmMgjl8IENfqcwmDZ==OeZobhfIg8VwZvc_5O4B8-pFPdi2o1e8kO=Nqm3uTwEZ-H6cyldNnetialBNU-ui9s9aWW7HWpdy3z=m_MHHXZIzebTCoiHvh612Nn-cyU5JtP1eG9ptjV8QNy2FsxemnL73OTctNP3FmPO3-i38J8illD0CJxYxoKcBG36aFCQO3vG2bj=nZA-HeuIww-lxg6BSM7nUFYEugXdTrOnSbPJXJnuuK86BiPHQ4Ok_E6qp1qY5jYuu8bz3Q_qs_IZjha=t=o8hQsGSMy2fKJozAuciMlPgDsh81YsLJnE1y6imiHcSgi-vOh4_Z6jfcSJZ40_FOhu70IjFXKvSO3SyEDH_7fDa186q2jdHP1HTK6mqFqyWKm9WM_aLfVSSJoL_SHVY7Ie1X1HkNXbnpjJ4zrZ30zeEw5QzWwyPvQZKCl10-o5lpq1x9Sih05hoxpH53uc=GQN8a=V7V=shetcjPdWo=kvtwPNNZ9xVA483iIbynCnxAV3KE1mmfDFoB4BdbKUkGKkiv0ghFiAoWP_FGpQttKGo91PqdqU=1Kw-JQfhXdauoSCxv19zmywgfSMKOGU9fCPrMj0d60QHTmkn-FI91rPD5kTZiLh-ucVaJH2wB9e-2oKexGl=gfZ2yTQu-9opA3zqkzu04gh4zHWCYTq0n3bSGPysHisySbHS6cTog4x5rLPYBdaCaTKMlQTbxoWWBEtGIwC-gg48e2ZlqOkMbmroTZboosCGrmZ2bZ_gOd35rYi4_37jOji9_QOSkyA5EblqVEZpZKwoVJBp1b5tC0Ow3T2D_-aVzXlL0rT31dkM5E4uMWigO2XKcOBSutpOlWX2UFKlLBofxGkdcA1A0eahd-pBlXEodxZVX6XgWmDNz=ATWeqEr0SH1AM7D6DTMKF2ut8iVc2srpdZDTFtX=qhO-jPPtD6nKpP19G00LV_vAyIIqa0aQebizyp0pVwH5IrXUQjADLeWAU8DwuEOa1g672hXoQQNon6=7r3jHmdduPgfJM4CgrpSyLhv7bKSbkjGPhWj5zcBXlE0HzXJado-CPMqJLIbDo-v0oUqojWJXL4wbYETsCfK=v7fUrAvUXM6SgtKoDs3BYMT5SqLThcJTvVhHog3DdkxaNgs-Few3zQI5SgJNtyzy96_s0-X4M-Da-ts9snvv=c3cJ-aP=vfkVzcKpkyMovdCkrqaBsvXZ-x22_jbf6_Km2OcX=O6rxfY2LqMdXYHuVW_I6SD64UcUJonHCCqNuvDAPcgkDcVe_7Aw2x0Fb8G-DZgBN44ka_iGKlbLE3Bg2ITttUiaC7brBsBxi6KMs_D5DgBZAVumV2nTF6b1hDdkN=vNMPvO2UoxTzWwuS127=qqTo3S6=Jsl85gZz7nw37hfgKxqaQ_z_=Jr2leVJMk66mJaqxb0QXKDt=UL3wWQn2XhKQhzM7oYPCku=u-4hSgTZXXqrnqrSeZf7KgUU2=c=xGDDm9Kjvt1tB-cpmSy=EvOgCbeVy9die3pkbTf6n-ja8zp_1hh3UGaN6mZ3d0tcMxqqnO-aUm=01SyEM5Z_hAeq8yPDKfb70OQPjpWG2cAIMvKvadfN1MaCa242sCjrOjpyAcbEbI_4Zj=lNdfX0K46_lZauWJLajuZxQtNZ777IaCKQn7EuaOGrfMKkvsEnUm12NakTiQ-4ZK9AZUPbXDV1gYwFuuJBEII-_08=n2u4NErpNyQL7XJIcdQ3x-3CxL0_aSL9zUkSbUdBh5hCvC5moHoAwCJzA_7BFWCar7ZY=tmx6Gvp7ZgyN3M=Jt88LFc_yLyyxKkPF-aC9MwUt-HLQw8r6Piwkx8gQu_yughU62ZzINvd_yfcfeQD4ff73gJJcTkmTKjydIbih18F2obF14f8-wuoftGI1tfPayXzTJskS-0KClV-Oq84O5lJldZPNBkMk_KYegs2O-zPC7OfILyZBsUx7P_8GdkSw7LuBWcyEnl8PodsqO6ba8r-LDePVVxJ_uvQ=543X-wwEsqET8G5BqmpAX3_oQVfdUz_xVchy8YN0Urye1gy0xPQ=G=IVc6EO=60mFJle4NZ-V0ttyqJCVB1zlAHW5flgNgkWIFhpvduHG2IMBoNp64dTMdogZu-9-iEpVKSaMe8rqHm-BojfFweWyuWnTBVOZqQJlQp_goyZ_L034K0Vqo61jWVQiHFNvkbcgIPBChiwDFhsL-XYQT9E4MlYVF657SaQVGDAuFF_klB=WnpnOiocsloGclfIsg9KF-M-ipJvKI0tEDVw_X4C6YTIiIWtxE6YtPEQUY2az-rynqasFZz0s-a=XL07VwhN43Kq34_=_sISzv81uDQ0oc1bT5bEp9EZB3NGUHoILALlGXz6oP6yPhroCUEJq_AgyWPDEhzsC11HLY3auQ64EAt0Hz2_7hb4LCceA2coLayONzSyjlcXIx60AIti5Sx9-bWpKbPuedgGU8DkJBaOLHE_0cwuS-2ntZHs9_I0ELh5s9UrlNtmZ1=XBuDyhuMtT4iDwTz1XGh1HT=FkC-fmqXmspc_U=y0D1yn7b5F1Ygr608u53H0fiWurs4dK-VQcVq37sm7QVvTEdis0Ch11-J4NU7CXpjm3SKoQgcLMZ3B6aa5Ydn2oguuia7BmTFBLCoUoWhcOWxkdiy6vsTZq_vPMw17T5B84vDtkahDpKMiZu0Ias7mfv9lES3JNXZ7faJh12hmwU1G9W5KBGGEZJh4rU25oj9ej6CWvj9QwJqs7K=wilO454kUsHqyfNLpAauLiXCQ_00C0r5_SPblLwYHJVpTQe7leotqoiOc7A39UtlIc_pYQVETmnZtavw0zXIelspZ=FsD3g-nsBsOqq5Pvw_SdZECDjCitwTN=YHAFoiZsDpIcPTcsBoieMgWbF1oY9lbnwjUdZjDmKv99rWjNyA6GHEDbw2hUNxQxrkpWZvc2vA46xr0krEqNNfCzNcK5Q-hg3Ye687jxprY-OxOZf-ZEHLonnI4dPjbNOkQb3yNEgYTjY96GMPA7pPciXfae7GykiVj6L0vOzWwBZoHKHNE3vWzvHCT5P6=6t=zZaE1FnmQyIwsMHOqCK5LnwasV1rflyKh=tPorWzqy=mmtaWyDn0Dx=yB=LtUNWOq1VxuXUA6mj-JeS=_dyWZA-xWixuU=MEdm=yKn3SUaIYDiJydn=CA2wJaTp_EQ3eNqG63KO4uxYeWx3dnsVWgCXSNMlZeQ3KnBEy4G9MbCjqee=h0_suwj6i4DxqrLGab3yTOsVezuT-41MGk1pFT7_FOTILchOx5nOHSP9WY5qO-lO-1AY8tw2_Q359HqH_BcL2oA0Xf8rt68ykunYyb50-885mhN39NrBqVrBCwPz2jNlTbvpskMfyWzptKS0CboJZdPqVqTgPbNojjmd1pk6HekV=izqp3ZSt1=oYDimxaTNY_rqkoT3GMz6oy0JJgVMBUObw-xnQQNgqzCwOLGcn4vkJg_rATVDeOfZIzyEZq=xgmgrZeYdq=Mjp80D_ZDv23Ee4tmgS3D4cg9nEBf1-sGMBMrsa8-Q1eNK5JeTM3_mJgre=LmpSCxPpTQ72XxZzPfOFjdX6AYK1zYKlKipTSzoDMDviBiI=e-stp9tlhzsf0HtXh8YP-mMEcra0eP8k_V0iD0D4uZXF_fn58dD=vJnI2bLolGUJ5cuof6_GK8IvNEvjywGWiCIb_P1l7tb86Qfbv6duHwblQAUOsggc-VIKAHUxqMv2hHvqi=qo_AcPm3mzPv9du_mWB_SKow6aaDUSdy4TB7arQuWkTgc6kXd8jbwquXao-ib61Wk-b1jL4_=SUNadrzQNlmVt2sU3tnTFBH1m-iHkk63DVBGplBgVd9OGpIonYbF8U4ea5hXHnujN01ouqbVdoAcW3-EAI6sPfwK9nDozt4m4A1-Zlb7wTIlGk=-_AcdxKdCU8AtV4VVyyDWKnmdyu2tPcWWNhGMrUL9IL0l6TbqWD92CU1iJ77-eGvLn_FTafoMXVaLM33lq3TPGbdUxnJhKpLYhYFg8gU2g5P8nMenkaQ1gPMG6PFGM834waBH5Nkf1IgMk3Wbp6=iUcPp9fB4VxF0UDVnOPeHbV1eqPyACTZAxn5wnA1rr5vOUboG4fNs7_BI1dkSoojig8zJd-3zOQwbUlSkm82AgaQUkcXGYYdeXlDh7o9BkqZ-3CwDNUXEnksViNONPXBDPF8ZaXSP7hxiqBUomcgzaApDjy1D6S4VxzlTK0_0SyhPa38yxA_D=nkA6=Acu4KuWll1gjyLPt2TD6GNNpGsb0d3eMEY0bBiVMAjGXckfYM1mxtNqISDMaea-Wwp-4NgoX3cZAe5c6MgbhIx09NB14v3IEMK4ijn==DaIurjF8ESGZP89wQvYsmQO5FmvVgSam82ac9-EcZY4k3VJgUpd_VEghQyEsjOsSv2wTVznI-wOXtEbMpxISfXEr2PZBaFNbwVDfYMPDi4wN-boeo_QXf7kn7AhOUu_lMqZYi9nQkBv=Yusu4Sk1FfCkGe7XBEMJxX2bAfuT8GxnSElgsldtEjhyvOn1ZnBJ_ZZyTztS99OI1h-0NnjVS4NEM=WB2gX=Ls5ITV9ddkAHTd4N5ftWskYI5XSCkqd84XvkDSIYVOZY7PYeKkCMHyESm1G=zHDysH3LJT6p7gyuKhnYp2Jkm9KPGPMGC7S=8-F6K3QpIgoc2It6OV8KuIa6t7BWDKGUjJ9=ZiTWrvXFStF2JgxckS9za4X7LBn9hSgMweovHSKIAPQHGcSjxB6KGWwLg8PnDE_10dgb1jp1o7XG0FKfAeF6d6QeXh=Ypjte78-rF2iSiNh4-gPsi1418QXubfcNdf=D2Li15v-Hgdez1S03ecUNwUV3Y1sYHH-8urffwC_s8acvacJG9x_Wy4A7ovol6_-ip3qBhBbLYwyn=QiX5=SlaqzyhuShIWIrAcLCNkughN=MOY-oY5wy2NTzIUYLVZyGam7ecl36v5ieaTwBBwjgixaf9_dNNtaP0AYnlYY3qOLH-ebtXyHSQGbLMCNYI30cI2=Lk7yHgBt2UQzKtyJm9lt5dBl8nniqQMTdqnB_3=P-Z11GuJtOt8UuqwcqmElthLlb=frHOpFlVC6VQV_ntBmV--ylbiVXrYi1FdrrUTDmvWrYCDd1gcvZKew=00IsQGSsBp9dcbOP8at-hQyTxbAnaQ7xi_S7l7G5dnQ_LEcSLnz_vU7BrDn7jkIHSvwZI-IKPTZyXys3_vSO9ZW4eg6C13YlzCSeqTJF5LvSOJcp96hwWzyhBZ9e9l2HS_fy6nmOVuqH87L1UoePJLOysfTF6u8xa=e3ZPfD0wvo4qzP2fdZmZ7Whr75wc3cC75nxm1N03aBkPDPSF7GOm",
           "X-C1agk3na-B": "eiyg97",
           "X-C1agk3na-C": "AMD6EZWNAQAAOJOq8Z7mLAzKjVZk6P7eySjAB8kTh_2MLrqL0bDTDPTuGhLQ",
           "X-C1agk3na-D": "ABaAhIDBCKGFgQGAAYIQgISigaIAwBGAzvpCzi_33wew0wz07hoS0AAAAABSQe9sANY312MFoKyu-c87h7ctOqA",
           "X-C1agk3na-F": "A0nhFJWNAQAA5FsMIHkhMWNTdiv1DYqcWSLbnGmFEnRGAQAnR9z2quDZCoBFAUOmNvWuclIDwH8AAEB3AAAAAA==",
           "X-C1agk3na-Z": "q",
           "Cookie": "aH1sihCg=A_V1FZWNAQAAXfVewKVVjRmhUEKwGGwL1FJxaxWtiyJfEapf5XrEkqfKalYOAUOmNvWuclIDwH8AAEB3AAAAAA|1|1|a24d5c1651019e2c791da76fd433094ee5d91757;",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
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
    "city": "Lakewood",
    "stateCode": "CO",
    "zipCode": "80401",
    "searchLocation": "Lakewood, CO 80401",
    "latitude": "39.73984822",
    "longitude": "-105.1969097",
    "limit": "20",
    "offset": "0",
    "searchCategoryType": "place-of-care",
    "categoryId": "91121",
    "fields": "providers,sortTypes,contextMessages,disclaimerCodes,alertCode",
    "channel": "public"
}
# Send the GET request with headers and params
response = requests.get(url, headers=headers, params=params)
print(response.text)
data = response.json()
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