import traceback
import requests
import json
from config.basic_conf import HEADER
from config.city_mapping import CITY
from config.route_mapping import ROUTES


def run(method, params):
    headers = HEADER
    city = CITY
    departure = params["departure"]
    destination = params["destination"]
    flight_date = params["flight_date"]

    try:
        url = ROUTES.get(method)
    except Exception as e:
        traceback.print_exc()

    request_payload = {
        "flightWay": "Oneway",
        "classType": "ALL",
        "hasChild": 'false',
        "hasBaby": 'false',
        "searchIndex": 1,
        "airportParams": [
            {
                "dcity": city.get(departure),
                "acity": city.get(destination),
                "dcityname": departure,
                "acityname": destination,
                "date": flight_date
            }
        ]
    }
    # 这里传进去的参数必须为 json 格式
    response = requests.post(url, data=json.dumps(request_payload), headers=headers).text
    routeList = json.loads(response).get('data').get('routeList')
    # 循环这个数据集合
    info_list = []
    for route in routeList:
        if len(route.get('legs')) == 1:
            info = {}
            legs = route.get('legs')[0]
            flight = legs.get('flight')

            cabins = legs.get('cabins')[0].get('price')
            price = cabins.get('price')
            # 存储到数据库中
            info_list.append({
                "airline_name": flight.get('airlineName'),
                "flight_number": flight.get('flightNumber'),
                "departure_airport_name": flight.get('departureAirportInfo').get('airportName'),
                "arrival_airport_name": flight.get('arrivalAirportInfo').get('airportName'),
                "departure_time": flight.get('departureDate'),
                "arrival_time": flight.get('arrivalDate'),
                "punctuality_date": flight.get('punctualityRate'),
                "price": price,
            })
            # print("路线：",airlineName,flightNumber,airportName,departureDate,arrivalDate,punctualityRate,price)
            # 路线： 吉祥航空 HO7340 成都天府国际机场 2023-11-24 20:00:00 2023-11-24 22:35:00  1090
    return info_list

