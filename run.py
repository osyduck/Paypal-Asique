#Osyduck

import requests, time, json, datetime

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



cookie = input("Cookie: ")
csrf = input("CSRF: ")
brp = int(input("Berapa kali loop: "))
print("\n\n")
print("Paypal Conversion by osyduck\n")
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
    print("[%s] Balance: %s$"%(x, balance))
