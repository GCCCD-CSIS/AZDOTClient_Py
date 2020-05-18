import requests
import math


#
# Calculate distance between latitude longitude pairs with Python
# https://gist.github.com/rochacbruno/2883505
#
def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371  # km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c
    return d


#
# Request Event data from info providerrm -rf
#
def req(url, key):
    payload = {'key': key, 'format': 'xml'}
    response = requests.get(url, params=payload)


    return response.json()


if __name__ == "__main__":
    origin = (34.866034, -111.763573)
    a = req('https://az511.com/api/v2/get/event', '***')
    # soft by distance from origin
    a.sort(key=lambda k: distance(origin, (k['Latitude'], k['Longitude'])))
    print(a[0])
