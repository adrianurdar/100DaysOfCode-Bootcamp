import requests
import os
from datetime import datetime, timedelta
from flight_data import FlightData

KIWI_SERVER = "https://tequila-api.kiwi.com"
headers = {
    "apikey": os.environ["apikey"],
}

# Search flight parameters
fly_from = "BUH"
date_from = datetime.now() + timedelta(days=1)
date_to = datetime.now() + timedelta(days=181)
nights_in_dst_from = 7
nights_in_dst_to = 28
flight_type = "round"
curr = "EUR"
max_stopovers = 0


class FlightSearch:
    def get_city_code(self, city_name):
        query_endpoint = f"{KIWI_SERVER}/locations/query"
        params = {
            "term": city_name,
            "location_types": "city",
        }
        res = requests.get(url=query_endpoint, headers=headers, params=params)
        city_code = res.json()["locations"][0]["code"]

        return city_code

    def search_cheapest_flight(self, city_code):
        query_endpoint = f"{KIWI_SERVER}/v2/search"
        try:
            params = {
                "fly_from": fly_from,
                "fly_to": city_code,
                "date_from": date_from.strftime("%d/%m/%Y"),
                "date_to": date_to.strftime("%d/%m/%Y"),
                "nights_in_dst_from": nights_in_dst_from,
                "nights_in_dst_to": nights_in_dst_to,
                "flight_type": flight_type,
                "curr": curr,
                "max_stopovers": max_stopovers,
            }
            res = requests.get(url=query_endpoint, headers=headers, params=params)
            data = res.json()['data'][0]

            cheapest_flight = FlightData(
                price=data['price'],
                city_from=data['cityFrom'],
                city_to=data['cityTo'],
                airport_from=data['flyFrom'],
                airport_to=data['flyTo'],
                departure_date=data['route'][0]['local_departure'].split('T')[0],
                return_date=data['route'][1]['local_arrival'].split('T')[0],
                via_city=""
            )
        except IndexError:
            params = {
                "fly_from": fly_from,
                "fly_to": city_code,
                "date_from": date_from.strftime("%d/%m/%Y"),
                "date_to": date_to.strftime("%d/%m/%Y"),
                "nights_in_dst_from": nights_in_dst_from,
                "nights_in_dst_to": nights_in_dst_to,
                "flight_type": flight_type,
                "curr": curr,
                "max_stopovers": 2,
            }
            res = requests.get(url=query_endpoint, headers=headers, params=params)
            data = res.json()['data'][0]

            cheapest_flight = FlightData(
                price=data['price'],
                city_from=data['cityFrom'],
                city_to=data['cityTo'],
                airport_from=data['flyFrom'],
                airport_to=data['flyTo'],
                departure_date=data['route'][0]['local_departure'].split('T')[0],
                return_date=data['route'][-1]['local_arrival'].split('T')[0],
                via_city=data["route"][0]["cityTo"]
            )

        return cheapest_flight
