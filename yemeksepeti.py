import requests
import time

url = "https://tr.fd-api.com/api/v6/incentives-wallet/vouchers/save?locale=tr_TR"
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "tr-TR,tr;q=0.9,uz-UZ;q=0.8,uz;q=0.7,en-US;q=0.6,en;q=0.5",
    "authorization": "BEARER İLE BAŞLAYAN TOKENL BURAYA",
    "content-type": "application/json;charset=UTF-8",
    "perseus-client-id": "1710195078933.51928591653721544.wwevx4vo6n",
    "perseus-session-id": "1710195152008.747998778786606200.cl8sw22hpl",
    "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "x-fp-api-key": "volo"
}

voucher_codes = [
"GRN58INR",
"GRN82YOW",


]

for code in voucher_codes:
    data = {"code": code}
    response = requests.post(url, headers=headers, json=data)
    print(f"Code: {code}, Response: {response.json()}")
    time.sleep(12)
