# Project 1

Web Programming with Python and JavaScript

DarkSky API
9c102d141a42e76829cf376926f239db

Google Maps API

export API_KEY=AIzaSyA9E7fqAbUSR_e3SOWirLbtrpvDisI_gDY

import requests
weather = requests.get("https://api.darksky.net/forecast/9c102d141a42e76829cf376926f239db/42.37,-71.11").json()
print(weather["currently"])


import requests, json
weather = requests.get("https://api.darksky.net/forecast/9c102d141a42e76829cf376926f239db/42.37,-71.11").json()
print(json.dumps(weather["currently"], indent = 2))


Sample of the Darksky JSON

{"latitude":37.8267,"longitude":-122.4233,
"timezone":"America/Los_Angeles",

"currently":{
"time":1530831027,
"summary":"Clear",
"icon":"clear-day",
"nearestStormDistance":149,
"nearestStormBearing":346,
"precipIntensity":0,
"precipProbability":0,"
temperature":70.01,
"apparentTemperature":70.01,
"dewPoint":53.41,
"humidity":0.56,
"pressure":1020.05,
"windSpeed":7.99,
"windGust":11.38,
"windBearing":282,
"cloudCover":0.05,
"uvIndex":6,
"visibility":10,
"ozone":304.47},
