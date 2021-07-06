import requests
import json

X_AUTH_TOKEN = "d3f8a4d46b53f81a9b995bce4e18ba85f3a26216"

<<<<<<< HEAD
ALLOWED_GROUPS = ["cdek_tt", "cdek_td", "dpd_tt", "dpd_td"]

=======
>>>>>>> master

class Shiptor:
    def __init__(self, access_token):
        self.__url = "https://api.shiptor.ru/shipping/v1"
        self.__headers = {
            "Content-Type": "application/json",
            "X-Authorization-Token": access_token,
        }

    def suggest_settlement(self, query, parent=None, country_code="RU"):
        payload = {
            "id": "JsonRpcClient.js",
            "jsonrpc": "2.0",
            "method": "suggestSettlement",
            "params": {"query": query, "country_code": country_code},
        }
<<<<<<< HEAD

        if parent:
            payload["params"]["parent"] = parent

        r = requests.post(self.__url, data=json.dumps(payload), headers=self.__headers)

        return json.loads(str.encode(r.text).decode("unicode-escape"))["result"]

    def calculate_shipping(
        self,
        length: int,
        width: int,
        height: int,
        weight: int,
        cod: int,
        kladr_id,
        courier=None,
    ):
        kladr_id_from = "1600000100000"
        country_code = "RU"

=======
        if parent:
            payload["params"]["parent"] = parent
        r = requests.post(self.__url, data=json.dumps(payload), headers=self.__headers)
        return json.loads(str.encode(r.text).decode("unicode-escape"))

    def calculate_shipping(
        self, length, width, height, weight, cod, kladr_id, courier
    ):
        kladr_id_from = "1600000100000"
        country_code = "RU"
        
>>>>>>> master
        payload = {
            "id": "JsonRpcClient.js",
            "jsonrpc": "2.0",
            "method": "calculateShipping",
            "params": {
                "stock": False,
                "kladr_id_from": kladr_id_from,
                "kladr_id": str(kladr_id),
                "length": length,
                "width": width,
                "height": height,
<<<<<<< HEAD
                "weight": weight / 1000,
                "cod": cod,
                "declared_cost": cod,
            },
        }

        if courier:
            payload["params"]["courier"] = courier

        print(payload)

        r = requests.post(self.__url, data=json.dumps(payload), headers=self.__headers)

        result = json.loads(str.encode(r.text).decode("unicode-escape"))["result"][
            "methods"
        ]

        result = [
            method
            for method in result
            if method["method"]["group"] in ALLOWED_GROUPS and method["status"] == "ok"
        ]

        return result


sh = Shiptor(X_AUTH_TOKEN)
=======
                "weight": weight,
                "cod": cod,
                "declared_cost": cod,
                "courier": courier
            }
        }
        r = requests.post(self.__url, data=json.dumps(payload), headers=self.__headers)
        with open("q.json", "wt") as f:
            f.write(str.encode(r.text).decode("unicode-escape"))
>>>>>>> master
