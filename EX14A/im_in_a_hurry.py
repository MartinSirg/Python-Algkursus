"""Retrieve stops and departures info from REST service."""

import json
import urllib.request

API_BASE = "https://public-transport-api.herokuapp.com"
REGION = "tallinn"


def get_nearby_stops(api_base, lat, lng):
    """
    Get nearby stops.

    :param api_base: Base URL that the endpoint gets appended to
    :param lat: Latitude
    :param lng: Longitude
    :return: List of all nearby stops
    """
    with urllib.request.urlopen(f"{api_base}/stops/{lat}/{lng}") as file:
        contents = file.read()
        data = json.loads(contents.decode("utf-8"))
        distance = []   # find shortest dist.
        for item in data:
            distance.append(int(item['distance'][:-2]))
        result = []
        while len(distance) > 0:
            index_of_min_len = distance.index(min(distance))
            result.append(data[index_of_min_len])
            distance.remove(distance[index_of_min_len])
            data.remove(data[index_of_min_len])
            print(result[-1]["name"] + " :  " + result[-1]["distance"])
        return result


def get_nearest_stop(api_base, lat, lng):
    """
    Get nearest stop.

    :param api_base: Base URL that the endpoint gets appended to
    :param lat: Latitude
    :param lng: Longitude
    :return: Nearest stop
    """
    result = get_nearby_stops(api_base, lat, lng)
    if len(result) == 0:
        return None
    return result[0]


def get_next_departures(api_base, region, stop_id):
    """
    Get next departures from stop.

    :param api_base: Base URL that the endpoint gets appended to
    :param region: Region
    :param stop_id: Stop ID
    :return: List of next departures from stop
    """
    with urllib.request.urlopen(f"{api_base}/departures/{region}/{stop_id}") as file:
        contents = file.read()
        decoded_contents = contents.decode("utf-8")
        data = json.loads(decoded_contents)
        return data["departures"]


def get_next_departure(api_base, region, stop_id):
    """
    Get next departure from stop.

    :param api_base: Base URL that the endpoint gets appended to
    :param region: Region
    :param stop_id: Stop ID
    :return: Next departure from stop
    """
    result = get_next_departures(api_base, region, stop_id)
    if len(result) == 0:
        return None
    return result[0]


lati, longi = 59.3969182, 24.6628295
print(get_nearby_stops(API_BASE, lati, longi))
