import requests

path = 'http://api.postcodes.io/postcodes/'
arguments = 'w1u4ed'


def long_lat(response):
    data_dict = response.json()
    result_dict = data_dict["result"]
    lat = result_dict['latitude']
    long = result_dict['longitude']
    output = f"Your longitude is {long} and your latitude is {lat}"

    return output

