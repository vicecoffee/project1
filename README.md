# Project 1

Web Programming with Python and JavaScript

DarkSky API
9c102d141a42e76829cf376926f239db

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

"minutely":{
"summary":"Clear for the hour.",
"icon":"clear-day",
"data":[{
"time":1530831000,
"precipIntensity":0,
"precipProbability":0},{"time":1530831060,"precipIntensity":0,"precipProbability":0},{"time":1530831120,"precipIntensity":0,"precipProbability":0},{"time":1530831180,"precipIntensity":0,"precipProbability":0},{"time":1530831240,"precipIntensity":0,"precipProbability":0},{"time":1530831300,"precipIntensity":0,"precipProbability":0},{"time":1530831360,"precipIntensity":0,"precipProbability":0},{"time":1530831420,"precipIntensity":0,"precipProbability":0},{"time":1530831480,"precipIntensity":0,"precipProbability":0},{"time":1530831540,"precipIntensity":0,"precipProbability":0},{"time":1530831600,"precipIntensity":0,"precipProbability":0},{"time":1530831660,"precipIntensity":0,"precipProbability":0},{"time":1530831720,"precipIntensity":0,"precipProbability":0},{"time":1530831780,"precipIntensity":0,"precipProbability":0},{"time":1530831840,"precipIntensity":0,"precipProbability":0},{"time":1530831900,"precipIntensity":0,"precipProbability":0},{"time":1530831960,"precipIntensity":0,"precipProbability":0},{"time":1530832020,"precipIntensity":0,"precipProbability":0},{"time":1530832080,"precipIntensity":0,"precipProbability":0},{"time":1530832140,"precipIntensity":0,"precipProbability":0},{"time":1530832200,"precipIntensity":0,"precipProbability":0},{"time":1530832260,"precipIntensity":0,"precipProbability":0},{"time":1530832320,"precipIntensity":0,"precipProbability":0},{"time":1530832380,"precipIntensity":0,"precipProbability":0},{"time":1530832440,"precipIntensity":0,"precipProbability":0},{"time":1530832500,"precipIntensity":0,"precipProbability":0},{"time":1530832560,"precipIntensity":0,"precipProbability":0},{"time":1530832620,"precipIntensity":0,"precipProbability":0},{"time":1530832680,"precipIntensity":0,"precipProbability":0},{"time":1530832740,"precipIntensity":0,"precipProbability":0},{"time":1530832800,"precipIntensity":0,"precipProbability":0},{"time":1530832860,"precipIntensity":0,"precipProbability":0},{"time":1530832920,"precipIntensity":0,"precipProbability":0},{"time":1530832980,"precipIntensity":0,"precipProbability":0},{"time":1530833040,"precipIntensity":0,"precipProbability":0},{"time":1530833100,"precipIntensity":0,"precipProbability":0},{"time":1530833160,"precipIntensity":0,"precipProbability":0},{"time":1530833220,"precipIntensity":0,"precipProbability":0},{"time":1530833280,"precipIntensity":0,"precipProbability":0},{"time":1530833340,"precipIntensity":0,"precipProbability":0},{"time":1530833400,"precipIntensity":0,"precipProbability":0},{"time":1530833460,"precipIntensity":0,"precipProbability":0},{"time":1530833520,"precipIntensity":0,"precipProbability":0},{"time":1530833580,"precipIntensity":0,"precipProbability":0},{"time":1530833640,"precipIntensity":0,"precipProbability":0},{"time":1530833700,"precipIntensity":0,"precipProbability":0},{"time":1530833760,"precipIntensity":0,"precipProbability":0},{"time":1530833820,"precipIntensity":0,"precipProbability":0},{"time":1530833880,"precipIntensity":0,"precipProbability":0},{"time":1530833940,"precipIntensity":0,"precipProbability":0},{"time":1530834000,"precipIntensity":0,"precipProbability":0},{"time":1530834060,"precipIntensity":0,"precipProbability":0},{"time":1530834120,"precipIntensity":0,"precipProbability":0},{"time":1530834180,"precipIntensity":0,"precipProbability":0},{"time":1530834240,"precipIntensity":0,"precipProbability":0},{"time":1530834300,"precipIntensity":0,"precipProbability":0},{"time":1530834360,"precipIntensity":0,"precipProbability":0},{"time":1530834420,"precipIntensity":0,"precipProbability":0},{"time":1530834480,"precipIntensity":0,"precipProbability":0},{"time":1530834540,"precipIntensity":0,"precipProbability":0},{"time":1530834600,"precipIntensity":0,"precipProbability":0}]},"hourly":{"summary":"Mostly cloudy starting this evening.","icon":"partly-cloudy-day","data":[{"time":1530828000,"summary":"Clear","icon":"clear-day","precipIntensity":0,"precipProbability":0,"temperature":69.28,"apparentTemperature":69.28,"dewPoint":53.58,"humidity":0.57,"pressure":1020.24,"windSpeed":7.2,"windGust":10.84,"windBearing":263,"cloudCover":0.07,"uvIndex":8,"visibility":10,"ozone":304.82},{"time":1530831600,"summary":"Clear","icon":"clear-day","precipIntensity":0.0004,"precipProbability":0.01,"precipType":"rain","temperature":70.14,"apparentTemperature":70.14,"dewPoint":53.37,"humidity":0.55,"pressure":1020.01,"windSpeed":8.23,"windGust":11.48,"windBearing":285,"cloudCover":0.05,"uvIndex":5,"visibility":10,"ozone":304.41},{"time":1530835200,"summary":"Clear","icon":"clear-day","precipIntensity":0.0011,"precipProbability":0.01,"precipType":"rain","temperature":69.34,"apparentTemperature":69.34,"dewPoint":53.43,"humidity":0.57,"pressure":1019.93,"windSpeed":8.11,"windGust":11.1,"windBearing":276,"cloudCover":0.06,"uvIndex":3,"visibility":10,"ozone":303.97},{"time":1530838800,"summary":"Clear","icon":"clear-day","precipIntensity":0,"precipProbability":0,"temperature":67.6,"apparentTemperature":67.6,"dewPoint":53.04,"humidity":0.6,"pressure":1019.93,"windSpeed":7.65,"windGust":11.18,"windBearing":261,"cloudCover":0.06,"uvIndex":1,"visibility":10,"ozone":303.32},{"time":1530842400,"summary":"Clear","icon":"clear-day","precipIntensity":0.0018,"precipProbability":0.01,"precipType":"rain","temperature":65.37,"apparentTemperature":65.37,"dewPoint":52.83,"humidity":0.64,"pressure":1019.94,"windSpeed":6.93,"windGust":11.07,"windBearing":278,"cloudCover":0.21,"uvIndex":1,"visibility":10,"ozone":302.77},{"time":1530846000,"summary":"Clear","icon":"clear-day","precipIntensity":0,"precipProbability":0,"temperature":63.47,"apparentTemperature":63.47,"dewPoint":52.83,"humidity":0.68,"pressure":1020.1,"windSpeed":6.48,"windGust":10.5,"windBearing":268,"cloudCover":0.22,"uvIndex":0,"visibility":10,"ozone":302.17},{"time":1530849600,"summary":"Partly Cloudy","icon":"partly-cloudy-night","precipIntensity":0,"precipProbability":0,"temperature":61.93,"apparentTemperature":61.93,"dewPoint":52.84,"humidity":0.72,"pressure":1020.44,"windSpeed":5.78,"windGust":8.95,"windBearing":255,"cloudCover":0.31,"uvIndex":0,"visibility":10,"ozone":301.9},{"time":1530853200,"summary":"Partly Cloudy","icon":"partly-cloudy-night","precipIntensity":0.001,"precipProbability":0.01,"precipType":"rain","temperature":60.78,"apparentTemperature":60.78,"dewPoint":52.73,"humidity":0.75,"pressure":1021.09,"windSpeed":5.36,"windGust":8.14,"windBearing":273,"cloudCover":0.38,"uvIndex":0,"visibility":10,"ozone":301.69},{"time":1530856800,"summary":"Partly Cloudy","icon":"partly-cloudy-night","precipIntensity":0.0016,"precipProbability":0.02,"precipType":"rain","temperature":59.77,"apparentTemperature":59.77,"dewPoint":52.69,"humidity":0.77,"pressure":1021.48,"windSpeed":4.9,"windGust":8.04,"windBearing":261,"cloudCover":0.44,"uvIndex":0,"visibility":10,"ozone":301.11},{"time":1530860400,"summary":"Partly Cloudy","icon":"partly-cloudy-night","precipIntensity":0,"precipProbability":0,"temperature":58.93,"apparentTemperature":58.93,"dewPoint":52.74,"humidity":0.8,"pressure":1021.59,"windSpeed":4.53,"windGust":6.77,"windBearing":271,"cloudCover":0.52,"uvIndex":0,"visibility":10,"ozone":299.71},{"time":1530864000,"summary":"Partly Cloudy","icon":"partly-cloudy-night","precipIntensity":0,"precipProbability":0,"temperature":58.58,"apparentTemperature":58.58,"dewPoint":52.89,"humidity":0.81,"pressure":1021.37,"windSpeed":4.3,"windGust":5.79,"windBearing":234,"cloudCover":0.59,"uvIndex":0,"visibility":10,"ozone":298},{"time":1530867600,"summary":"Mostly Cloudy","icon":"partly-cloudy-night","precipIntensity":0,"precipProbability":0,"temperature":58.45,"apparentTemperature":58.45,"dewPoint":53,"humidity":0.82,"pressure":1021.15,"windSpeed":4.05,"windGust":5.05,"windBearing":248,"cloudCover":0.72,"uvIndex":0,"visibility":10,"ozone":296.34},{"time":1530871200,"summary":"Mostly Cloudy","icon":"partly-cloudy-night","precipIntensity":0,"precipProbability":0,"temperature":58.35,"apparentTemperature":58.35,"dewPoint":52.97,"humidity":0.82,"pressure":1020.98,"windSpeed":3.9,"windGust":5.04,"windBearing":256,"cloudCover":0.7,"uvIndex":0,"visibility":10,"ozone":295.14},{"time":1530874800,"summary":"Mostly Cloudy","icon":"partly-cloudy-night","precipIntensity":0.0003,"precipProbability":0.02,"precipType":"rain","temperature":57.99,"apparentTemperature":57.99,"dewPoint":52.93,"humidity":0.83,"pressure":1020.63,"windSpeed":3.43,"windGust":4.71,"windBearing":279,"cloudCover":0.77,"uvIndex":0,"visibility":10,"ozone":294.07},{"time":1530878400,"summary":"Mostly Cloudy","icon":"partly-cloudy-night","precipIntensity":0,"precipProbability":0,"temperature":58.09,"apparentTemperature":58.09,"dewPoint":52.95,"humidity":0.83,"pressure":1020.33,"windSpeed":3.4,"windGust":3.82,"windBearing":259,"cloudCover":0.84,"uvIndex":0,"visibility":10,"ozone":293.32},{"time":1530882000,"summary":"Overcast","icon":"cloudy","precipIntensity":0,"precipProbability":0,"temperature":58.02,"apparentTemperature":58.02,"dewPoint":53.5,"humidity":0.85,"pressure":1020.57,"windSpeed":3.58,"windGust":4.03,"windBearing":268,"cloudCover":0.96,"uvIndex":0,"visibility":10,"ozone":292.99},{"time":1530885600,"summary":"Overcast","icon":"cloudy","precipIntensity":0,"precipProbability":0,"temperature":58.59,"apparentTemperature":58.59,"dewPoint":53.64,"humidity":0.84,"pressure":1020.77,"windSpeed":3.37,"windGust":3.61,"windBearing":298,"cloudCover":0.95,"uvIndex":0,"visibility":10,"ozone":293.03},{"time":1530889200,"summary":"Overcast","icon":"cloudy","precipIntensity":0,"precipProbability":0,"temperature":59.57,"apparentTemperature":59.57,"dewPoint":53.74,"humidity":0.81,"pressure":1020.94,"windSpeed":2.79,"windGust":3.59,"windBearing":283,"cloudCover":0.95,"uvIndex":1,"visibility":10,"ozone":292.81},{"time":1530892800,"summary":"Overcast","icon":"cloudy","precipIntensity":0,"precipProbability":0,"temperature":61.44,"apparentTemperature":61.44,"dewPoint":53.76,"humidity":0.76,"pressure":1020.93,"windSpeed":2.41,"windGust":4.11,"windBearing":333,"cloudCover":0.96,"uvIndex":1,"visibility":10,"ozone":292.25},{"time":1530896400,"summary":"Overcast","icon":"cloudy","precipIntensity":0.001,"precipProbability":0.02,"precipType":"rain","temperature":63.45,"apparentTemperature":63.45,"dewPoint":53.74,"humidity":0.71,"pressure":1020.81,"windSpeed":2.3,"windGust":5.02,"windBearing":248,"cloudCover":0.98,"uvIndex":2,"visibility":10,"ozone":291.51},{"time":1530900000,"summary":"Overcast","icon":"cloudy","precipIntensity":0,"precipProbability":0,"temperature":65.61,"apparentTemperature":65.61,"dewPoint":53.73,"humidity":0.66,"pressure":1020.74,"windSpeed":4.11,"windGust":6.12,"windBearing":285,"cloudCover":1,"uvIndex":4,"visibility":10,"ozone":290.84},{"time":1530903600,"summary":"Overcast","icon":"cloudy","precipIntensity":0,"precipProbability":0,"temperature":67.65,"apparentTemperature":67.65,"dewPoint":53.78,"humidity":0.61,"pressure":1020.52,"windSpeed":4.96,"windGust":7.35,"windBearing":282,"cloudCover":0.99,"uvIndex":6,"visibility":10,"ozone":290.23},{"time":1530907200,"summary":"Overcast","icon":"cloudy","precipIntensity":0,"precipProbability":0,"temperature":69.84,"apparentTemperature":69.84,"dewPoint":53.85,"humidity":0.57,"pressure":1020.36,"windSpeed":5.78,"windGust":8.76,"windBearing":288,"cloudCover":0.98,"uvIndex":7,"visibility":10,"ozone":289.7},{"time":1530910800,"summary":"Overcast","icon":"cloudy","precipIntensity":0,"precipProbability":0,"temperature":70.87,"apparentTemperature":70.87,"dewPoint":53.89,"humidity":0.55,"pressure":1020.07,"windSpeed":7.19,"windGust":10.24,"windBearing":276,"cloudCover":0.97,"uvIndex":6,"visibility":10,"ozone":289.11},{"time":1530914400,"summary":"Overcast","icon":"cloudy","precipIntensity":0,"precipProbability":0,"temperature":71.46,"apparentTemperature":71.46,"dewPoint":53.82,"humidity":0.54,"pressure":1019.71,"windSpeed":7.31,"windGust":12.04,"windBearing":264,"cloudCover":0.95,"uvIndex":5,"visibility":10,"ozone":288.65},{"time":1530918000,"summary":"Mostly Cloudy","icon":"partly-cloudy-day","precipIntensity":0,"precipProbability":0,"temperature":70.83,"apparentTemperature":70.83,"dewPoint":53.72,"humidity":0.55,"pressure":1019.24,"windSpeed":8.85,"windGust":13.9,"windBearing":277,"cloudCover":0.93,"uvIndex":3,"visibility":10,"ozone":288.21},{"time":1530921600,"summary":"Mostly Cloudy","icon":"partly-cloudy-day","precipIntensity":0,"precipProbability":0,"temperature":69.71,"apparentTemperature":69.71,"dewPoint":53.7,"humidity":0.57,"pressure":1018.8,"windSpeed":9.34,"windGust":14.92,"windBearing":275,"cloudCover":0.91,"uvIndex":2,"visibility":10,"ozone":287.69},{"time":1530925200,"summary":"Mostly Cloudy","icon":"partly-cloudy-day","precipIntensity":0,"precipProbability":0,"temperature":68.21,"apparentTemperature":68.21,"dewPoint":53.86,"humidity":0.6,"pressure":1018.4,"windSpeed":9.04,"windGust":14.52,"windBearing":279,"cloudCover":0.87,"uvIndex":1,"visibility":10,"ozone":286.68},{"time":1530928800,"summary":"Mostly Cloudy","icon":"partly-cloudy-day","precipIntensity":0,"precipProbability":0,"temperature":66.54,"apparentTemperature":66.54,"dewPoint":54.09,"humidity":0.64,"pressure":1018.24,"windSpeed":8.36,"windGust":13.31,"windBearing":271,"cloudCover":0.82,"uvIndex":0,"visibility":10,"ozone":285.5},{"time":1530932400,"summary":"Mostly Cloudy","icon":"partly-cloudy-day","precipIntensity":0,"precipProbability":0,"temperature":64.89,"apparentTemperature":64.89,"dewPoint":54.22,"humidity":0.68,"pressure":1018.16,"windSpeed":7.59,"windGust":12.14,"windBearing":272,"cloudCover":0.73,"uvIndex":0,"visibility":10,"ozone":284.67},{"time":1530936000,"summary":"Partly Cloudy","icon":"partly-cloudy-night","precipIntensity":0,"precipProbability":0,"temperature":63.61,"apparentTemperature":63.61,"dewPoint":54.16,"humidity":0.71,"pressure":1018.27,"windSpeed":6.93,"windGust":11.31,"windBearing":270,"cloudCover":0.58,"uvIndex":0,"visibility":10,"ozone":284.28},{"time":1530939600,"summary":"Mostly Cloudy","icon":"partly-cloudy-night","precipIntensity":0,"precipProbability":0,"temperature":62.29,"apparentTemperature":62.29,"dewPoint":53.98,"humidity":0.74,"pressure":1018.54,"windSpeed":6.42,"windGust":10.54,"windBearing":270,"cloudCover":0.61,"uvIndex":0,"visibility":10,"ozone":284.25},{"time":1530943200,"summary":"Mostly Cloudy","icon":"partly-cloudy-night","precipIntensity":0,"precipProbability":0,"temperature":61,"apparentTemperature":61,"dewPoint":53.77,"humidity":0.77,"pressure":1018.63,"windSpeed":6.14,"windGust":9.83,"windBearing":268,"cloudCover":0.64,"uvIndex":0,"visibility":10,"ozone":283.99},{"time":1530946800,"summary":"Mostly Cloudy","icon":"partly-cloudy-night","precipIntensity":0,"precipProbability":0,"temperature":59.9,"apparentTemperature":59.9,"dewPoint":53.53,"humidity":0.79,"pressure":1018.55,"windSpeed":5.84,"windGust":9.17,"windBearing":267,"cloudCover":0.63,"uvIndex":0,"visibility":10,"ozone":283.55},{"time":1530950400,"summary":"Mostly Cloudy","icon":"partly-cloudy-night","precipIntensity":0,"precipProbability":0,"temperature":58.86,"apparentTemperature":58.86,"dewPoint":53.28,"humidity":0.82,"pressure":1018.37,"windSpeed":5.29,"windGust":8.6,"windBearing":282,"cloudCover":0.66,"uvIndex":0,"visibility":10,"ozone":283},{"time":1530954000,"summary":"Mostly Cloudy","icon":"partly-cloudy-night","precipIntensity":0,"precipProbability":0,"temperature":58.01,"apparentTemperature":58.01,"dewPoint":53.02,"humidity":0.83,"pressure":1018.12,"windSpeed":5.65,"windGust":8.2,"windBearing":274,"cloudCover":0.65,"uvIndex":0,"visibility":10,"ozone":282.53},{"time":1530957600,"summary":"Mostly Cloudy","icon":"partly-cloudy-night","precipIntensity":0.0002,"precipProbability":0.01,"precipType":"rain","temperature":57.13,"apparentTemperature":57.13,"dewPoint":52.74,"humidity":0.85,"pressure":1017.82,"windSpeed":5.48,"windGust":8.19,"windBearing":274,"cloudCover":0.64,"uvIndex":0,"visibility":10,"ozone":282.27},{"time":1530961200,"summary":"Mostly Cloudy","icon":"partly-cloudy-night","precipIntensity":0.0004,"precipProbability":0.01,"precipType":"rain","temperature":56.25,"apparentTemperature":56.25,"dewPoint":52.48,"humidity":0.87,"pressure":1017.54,"windSpeed":5.61,"windGust":8.35,"windBearing":276,"cloudCover":0.65,"uvIndex":0,"visibility":10,"ozone":282.05},{"time":1530964800,"summary":"Mostly Cloudy","icon":"partly-cloudy-night","precipIntensity":0.0006,"precipProbability":0.01,"precipType":"rain","temperature":55.67,"apparentTemperature":55.67,"dewPoint":52.28,"humidity":0.88,"pressure":1017.31,"windSpeed":5.47,"windGust":8.29,"windBearing":278,"cloudCover":0.72,"uvIndex":0,"visibility":10,"ozone":281.88},{"time":1530968400,"summary":"Mostly Cloudy","icon":"partly-cloudy-day","precipIntensity":0.0006,"precipProbability":0.01,"precipType":"rain","temperature":55.53,"apparentTemperature":55.53,"dewPoint":52.23,"humidity":0.89,"pressure":1017.37,"windSpeed":5.09,"windGust":7.65,"windBearing":275,"cloudCover":0.74,"uvIndex":0,"visibility":10,"ozone":281.71},{"time":1530972000,"summary":"Mostly Cloudy","icon":"partly-cloudy-day","precipIntensity":0.0005,"precipProbability":0.01,"precipType":"rain","temperature":56.02,"apparentTemperature":56.02,"dewPoint":52.25,"humidity":0.87,"pressure":1017.56,"windSpeed":4.41,"windGust":6.77,"windBearing":272,"cloudCover":0.71,"uvIndex":0,"visibility":10,"ozone":281.41},{"time":1530975600,"summary":"Partly Cloudy","icon":"partly-cloudy-day","precipIntensity":0.0004,"precipProbability":0.01,"precipType":"rain","temperature":57.38,"apparentTemperature":57.38,"dewPoint":52.32,"humidity":0.83,"pressure":1017.71,"windSpeed":4.37,"windGust":6.17,"windBearing":277,"cloudCover":0.59,"uvIndex":1,"visibility":10,"ozone":281.22},{"time":1530979200,"summary":"Partly Cloudy","icon":"partly-cloudy-day","precipIntensity":0.0002,"precipProbability":0.01,"precipType":"rain","temperature":59.27,"apparentTemperature":59.27,"dewPoint":52.45,"humidity":0.78,"pressure":1017.75,"windSpeed":4.18,"windGust":6.03,"windBearing":291,"cloudCover":0.51,"uvIndex":2,"visibility":10,"ozone":281.18},{"time":1530982800,"summary":"Partly Cloudy","icon":"partly-cloudy-day","precipIntensity":0,"precipProbability":0,"temperature":61.57,"apparentTemperature":61.57,"dewPoint":52.66,"humidity":0.73,"pressure":1017.73,"windSpeed":4.56,"windGust":6.17,"windBearing":255,"cloudCover":0.42,"uvIndex":3,"visibility":10,"ozone":281.14},{"time":1530986400,"summary":"Partly Cloudy","icon":"partly-cloudy-day","precipIntensity":0,"precipProbability":0,"temperature":63.88,"apparentTemperature":63.88,"dewPoint":52.76,"humidity":0.67,"pressure":1017.68,"windSpeed":5.17,"windGust":6.81,"windBearing":260,"cloudCover":0.33,"uvIndex":6,"visibility":10,"ozone":281.13},{"time":1530990000,"summary":"Partly Cloudy","icon":"partly-cloudy-day","precipIntensity":0,"precipProbability":0,"temperature":66.1,"apparentTemperature":66.1,"dewPoint":52.65,"humidity":0.62,"pressure":1017.48,"windSpeed":6.07,"windGust":8.21,"windBearing":261,"cloudCover":0.26,"uvIndex":9,"visibility":10,"ozone":281.13},{"time":1530993600,"summary":"Partly Cloudy","icon":"partly-cloudy-day","precipIntensity":0,"precipProbability":0,"temperature":68.32,"apparentTemperature":68.32,"dewPoint":52.43,"humidity":0.57,"pressure":1017.14,"windSpeed":7.21,"windGust":10.07,"windBearing":260,"cloudCover":0.31,"uvIndex":10,"visibility":10,"ozone":281.05},{"time":1530997200,"summary":"Partly Cloudy","icon":"partly-cloudy-day","precipIntensity":0,"precipProbability":0,"temperature":69.68,"apparentTemperature":69.68,"dewPoint":52.27,"humidity":0.54,"pressure":1016.67,"windSpeed":8.14,"windGust":11.7,"windBearing":258,"cloudCover":0.33,"uvIndex":9,"visibility":10,"ozone":281.06},{"time":1531000800,"summary":"Partly Cloudy","icon":"partly-cloudy-day","precipIntensity":0,"precipProbability":0,"temperature":70.28,"apparentTemperature":70.28,"dewPoint":52.18,"humidity":0.53,"pressure":1016.03,"windSpeed":8.76,"windGust":12.91,"windBearing":260,"cloudCover":0.4,"uvIndex":7,"visibility":10,"ozone":281.07}]},"daily":{"summary":"No precipitation throughout the week, with high temperatures bottoming out at 68°F on Sunday.","icon":"clear-day","data":[{"time":1530774000,"summary":"Mostly cloudy in the morning.","icon":"partly-cloudy-day","sunriseTime":1530795283,"sunsetTime":1530848177,"moonPhase":0.74,"precipIntensity":0.0002,"precipIntensityMax":0.0018,"precipIntensityMaxTime":1530842400,"precipProbability":0.01,"precipType":"rain","temperatureHigh":70.14,"temperatureHighTime":1530831600,"temperatureLow":57.99,"temperatureLowTime":1530874800,"apparentTemperatureHigh":70.14,"apparentTemperatureHighTime":1530831600,"apparentTemperatureLow":57.99,"apparentTemperatureLowTime":1530874800,"dewPoint":52.27,"humidity":0.75,"pressure":1019.68,"windSpeed":5.48,"windGust":12.89,"windGustTime":1530824400,"windBearing":262,"cloudCover":0.39,"uvIndex":11,"uvIndexTime":1530820800,"visibility":10,"ozone":305.4,"temperatureMin":54.03,"temperatureMinTime":1530784800,"temperatureMax":70.14,"temperatureMaxTime":1530831600,"apparentTemperatureMin":54.03,"apparentTemperatureMinTime":1530784800,"apparentTemperatureMax":70.14,"apparentTemperatureMaxTime":1530831600},{"time":1530860400,"summary":"Mostly cloudy throughout the day.","icon":"partly-cloudy-day","sunriseTime":1530881716,"sunsetTime":1530934563,"moonPhase":0.77,"precipIntensity":0.0001,"precipIntensityMax":0.001,"precipIntensityMaxTime":1530896400,"precipProbability":0.06,"precipType":"rain","temperatureHigh":71.46,"temperatureHighTime":1530914400,"temperatureLow":55.53,"temperatureLowTime":1530968400,"apparentTemperatureHigh":71.46,"apparentTemperatureHighTime":1530914400,"apparentTemperatureLow":55.53,"apparentTemperatureLowTime":1530968400,"dewPoint":53.6,"humidity":0.71,"pressure":1019.99,"windSpeed":5.25,"windGust":14.92,"windGustTime":1530921600,"windBearing":273,"cloudCover":0.83,"uvIndex":7,"uvIndexTime":1530907200,"visibility":10,"ozone":290.54,"temperatureMin":57.99,"temperatureMinTime":1530874800,"temperatureMax":71.46,"temperatureMaxTime":1530914400,"apparentTemperatureMin":57.99,"apparentTemperatureMinTime":1530874800,"apparentTemperatureMax":71.46,"apparentTemperatureMaxTime":1530914400},{"time":1530946800,"summary":"Partly cloudy throughout the day.","icon":"partly-cloudy-day","sunriseTime":1530968151,"sunsetTime":1531020947,"moonPhase":0.8,"precipIntensity":0.0002,"precipIntensityMax":0.0006,"precipIntensityMaxTime":1530968400,"precipProbability":0.02,"precipType":"rain","temperatureHigh":70.28,"temperatureHighTime":1531000800,"temperatureLow":54.19,"temperatureLowTime":1531054800,"apparentTemperatureHigh":70.28,"apparentTemperatureHighTime":1531000800,"apparentTemperatureLow":54.19,"apparentTemperatureLowTime":1531054800,"dewPoint":52.6,"humidity":0.72,"pressure":1016.61,"windSpeed":6.48,"windGust":14.4,"windGustTime":1531008000,"windBearing":266,"cloudCover":0.44,"uvIndex":10,"uvIndexTime":1530993600,"visibility":10,"ozone":282.37,"temperatureMin":55.53,"temperatureMinTime":1530968400,"temperatureMax":70.28,"temperatureMaxTime":1531000800,"apparentTemperatureMin":55.53,"apparentTemperatureMinTime":1530968400,"apparentTemperatureMax":70.28,"apparentTemperatureMaxTime":1531000800},{"time":1531033200,"summary":"Partly cloudy in the morning.","icon":"partly-cloudy-day","sunriseTime":1531054586,"sunsetTime":1531107329,"moonPhase":0.84,"precipIntensity":0.0001,"precipIntensityMax":0.0004,"precipIntensityMaxTime":1531054800,"precipProbability":0.01,"precipType":"rain","temperatureHigh":68.05,"temperatureHighTime":1531090800,"temperatureLow":54.62,"temperatureLowTime":1531137600,"apparentTemperatureHigh":68.05,"apparentTemperatureHighTime":1531090800,"apparentTemperatureLow":54.62,"apparentTemperatureLowTime":1531137600,"dewPoint":53.07,"humidity":0.77,"pressure":1015.1,"windSpeed":7.36,"windGust":15.65,"windGustTime":1531094400,"windBearing":259,"cloudCover":0.21,"uvIndex":10,"uvIndexTime":1531080000,"visibility":10,"ozone":298.8,"temperatureMin":54.19,"temperatureMinTime":1531054800,"temperatureMax":68.05,"temperatureMaxTime":1531090800,"apparentTemperatureMin":54.19,"apparentTemperatureMinTime":1531054800,"apparentTemperatureMax":68.05,"apparentTemperatureMaxTime":1531090800},{"time":1531119600,"summary":"Clear throughout the day.","icon":"clear-day","sunriseTime":1531141023,"sunsetTime":1531193710,"moonPhase":0.88,"precipIntensity":0,"precipIntensityMax":0,"precipProbability":0,"temperatureHigh":72.36,"temperatureHighTime":1531173600,"temperatureLow":55.06,"temperatureLowTime":1531224000,"apparentTemperatureHigh":72.36,"apparentTemperatureHighTime":1531173600,"apparentTemperatureLow":55.06,"apparentTemperatureLowTime":1531224000,"dewPoint":52.18,"humidity":0.7,"pressure":1014.78,"windSpeed":5.11,"windGust":12.89,"windGustTime":1531177200,"windBearing":257,"cloudCover":0,"uvIndex":11,"uvIndexTime":1531166400,"visibility":10,"ozone":305.84,"temperatureMin":54.62,"temperatureMinTime":1531137600,"temperatureMax":72.36,"temperatureMaxTime":1531173600,"apparentTemperatureMin":54.62,"apparentTemperatureMinTime":1531137600,"apparentTemperatureMax":72.36,"apparentTemperatureMaxTime":1531173600},{"time":1531206000,"summary":"Mostly cloudy overnight.","icon":"partly-cloudy-night","sunriseTime":1531227460,"sunsetTime":1531280088,"moonPhase":0.91,"precipIntensity":0,"precipIntensityMax":0,"precipProbability":0,"temperatureHigh":73.84,"temperatureHighTime":1531260000,"temperatureLow":54.38,"temperatureLowTime":1531310400,"apparentTemperatureHigh":73.84,"apparentTemperatureHighTime":1531260000,"apparentTemperatureLow":54.38,"apparentTemperatureLowTime":1531310400,"dewPoint":52.72,"humidity":0.69,"pressure":1013.7,"windSpeed":4.44,"windGust":11.14,"windGustTime":1531263600,"windBearing":248,"cloudCover":0.02,"uvIndex":11,"uvIndexTime":1531252800,"visibility":10,"ozone":298.73,"temperatureMin":55.06,"temperatureMinTime":1531224000,"temperatureMax":73.84,"temperatureMaxTime":1531260000,"apparentTemperatureMin":55.06,"apparentTemperatureMinTime":1531224000,"apparentTemperatureMax":73.84,"apparentTemperatureMaxTime":1531260000},{"time":1531292400,"summary":"Mostly cloudy throughout the day.","icon":"partly-cloudy-day","sunriseTime":1531313899,"sunsetTime":1531366465,"moonPhase":0.95,"precipIntensity":0,"precipIntensityMax":0.0002,"precipIntensityMaxTime":1531321200,"precipProbability":0,"temperatureHigh":68.56,"temperatureHighTime":1531346400,"temperatureLow":55.98,"temperatureLowTime":1531400400,"apparentTemperatureHigh":68.56,"apparentTemperatureHighTime":1531346400,"apparentTemperatureLow":55.98,"apparentTemperatureLowTime":1531400400,"dewPoint":53.41,"humidity":0.78,"pressure":1012.92,"windSpeed":5.4,"windGust":11.19,"windGustTime":1531350000,"windBearing":233,"cloudCover":0.59,"uvIndex":9,"uvIndexTime":1531339200,"visibility":10,"ozone":292.7,"temperatureMin":54.38,"temperatureMinTime":1531310400,"temperatureMax":68.56,"temperatureMaxTime":1531346400,"apparentTemperatureMin":54.38,"apparentTemperatureMinTime":1531310400,"apparentTemperatureMax":68.56,"apparentTemperatureMaxTime":1531346400},{"time":1531378800,"summary":"Mostly cloudy until afternoon.","icon":"partly-cloudy-day","sunriseTime":1531400339,"sunsetTime":1531452841,"moonPhase":0.99,"precipIntensity":0.0002,"precipIntensityMax":0.0006,"precipIntensityMaxTime":1531411200,"precipProbability":0.08,"precipType":"rain","temperatureHigh":69.23,"temperatureHighTime":1531432800,"temperatureLow":57.72,"temperatureLowTime":1531483200,"apparentTemperatureHigh":69.23,"apparentTemperatureHighTime":1531432800,"apparentTemperatureLow":57.72,"apparentTemperatureLowTime":1531483200,"dewPoint":54.76,"humidity":0.8,"pressure":1013.15,"windSpeed":5.07,"windGust":11.39,"windGustTime":1531440000,"windBearing":232,"cloudCover":0.42,"uvIndex":10,"uvIndexTime":1531429200,"visibility":10,"ozone":299.22,"temperatureMin":55.98,"temperatureMinTime":1531400400,"temperatureMax":69.23,"temperatureMaxTime":1531432800,"apparentTemperatureMin":55.98,"apparentTemperatureMinTime":1531400400,"apparentTemperatureMax":69.23,"apparentTemperatureMaxTime":1531432800}]},"alerts":[{"title":"Beach Hazards Statement","regions":["Coastal North Bay Including Point Reyes National Seashore","Northern Monterey Bay","San Francisco","San Francisco Peninsula Coast","San Fransisco Peninsula Coast","Southern Monterey Bay and Big Sur Coast"],"severity":"watch","time":1530806340,"expires":1531000800,"description":"...Long Period Southerly Swell through Saturday... .A moderate-sized long-period southerly swell generated by Hurricane Fabio will continue to impact the Central Coast Thursday and continue into the weekend. The largest southerly waves are forecast to arrive late Thursday into early Friday. ...BEACH HAZARDS STATEMENT REMAINS IN EFFECT THROUGH SATURDAY AFTERNOON... * WAVES AND SURF...Southerly swell 4 to 7 feet with a period of 16 to 18 seconds. * HAZARDS...Increased risk of rip currents and sneaker waves, stronger longshore current at west facing beaches, and somewhat larger breaking waves at south facing coasts. * TIMING...Forerunners will arrive late tonight through early Thursday morning. The larger waves arrive later Thursday into early Friday. Waves will diminish through the day Saturday. * LOCATION...Primarily south facing coastal sections of Marin and Santa Cruz counties. In particular southwest facing beaches... including but not limited to...Stinson Beach... Santa Cruz Boardwalk Beach and Twin Lakes Beach. * POTENTIAL IMPACTS...Increased risk of drowning or being pulled out to sea by this energetic swell train. Never turn your back on the ocean!\n","uri":"https://alerts.weather.gov/cap/wwacapget.php?x=CA125AAFC31B3C.BeachHazardsStatement.125AAFE29A20CA.MTRCFWMTR.9d1f6acb9dca5e256fc7581df00a2ad7"}],"flags":{"sources":["nearest-precip","nwspa","cmc","gfs","hrrr","icon","isd","madis","nam","sref","darksky"],"nearest-station":1.839,"units":"us"},"offset":-7}# project1
