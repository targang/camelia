import requests

url = "https://api.boxberry.ru/json.php"

params = {
    "token": "d6f33e419c16131e5325cbd84d5d6000",
    "method": "DeliveryCosts",
    "weight": "500",
    "targetstart": "010",
    "target": "011",
    "ordersum": "0",
    "deliverysum": "0",
    "height": "20",
    "width": "40",
    "depth": "30",
    "paysum": "100",
}

payload = {}

headers = {}

r = requests.get(url, params=params, data=payload, headers=headers)

print(r.text)
