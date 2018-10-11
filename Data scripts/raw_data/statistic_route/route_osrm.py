import requests
import json

def calRoutes(start, stop):
    url = 'http://router.project-osrm.org/route/v1/driving/' + start + ';' + stop + '?geometries=geojson&overview=simplified&steps=false'
    response = requests.get(url)
    data = response.json()
    try:
        routes = data["routes"][0]["geometry"]
        return routes
    except KeyError:
        return

start = '-87.683593,41.991178'
stop = '-87.5761197602,41.78101637196'
routes = calRoutes(start, stop)
print(routes)

json.dumps(routes,sort_keys=True,indent=4)