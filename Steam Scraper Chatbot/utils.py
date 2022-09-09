import requests


def get_info(from_, to, amount) -> dict:
    #To = 'NGN'
    #From = 'GHS'
    #Amount = 10

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}"

    payload = {}
    headers = {
        "apikey": "u1mKpviY5eVaWwTp6bhv2ytEpiE8xPSZ"
    }

    response = requests.request(
        "GET", url,          headers=headers, data=payload)

    status_code = response.status_code
    result = response.json()

    to_currency = result['query']['to']
    from_currency = result['query']['from']
    amount_currency = result['query']['amount']

    rate = result['info']['rate']

    output = {"Exchange": [to_currency, from_currency, amount_currency, rate]}

    return output
