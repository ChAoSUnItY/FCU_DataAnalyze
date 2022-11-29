import requests as req

def convert(from_, amount):
    url = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}"
    payload = {}
    headers= {
        "apikey": "Hjf1XK00qfRg1IpyBfur2534z3i9ULUF"
    }
    respond = req.request('GET', url.format(to='USD', from_=from_, amount=amount), headers=headers, data = payload).json()
    print(respond)
    return respond['result']