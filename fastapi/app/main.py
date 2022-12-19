from fastapi import FastAPI, Response
import requests
import infoclimat as infoclimat
import etcd # pip install python-etcd

app = FastAPI()

@app.get("/")
async def root():
    metaDataStationMeteo = getMetaDataStationMeteo()
    token = getTokenApiMeteo()
    prometheusData = buildReponsePrometheus(metaDataStationMeteo, token)
    return Response(content=prometheusData, media_type="text/plain")

def buildReponsePrometheus(metaDataStationMeteo, token):
    return "temperature{station=\"" + metaDataStationMeteo["name"] + "\"} " + getTemperatureDepuisApi(metaDataStationMeteo, token)

def getTemperatureDepuisApi(metaDataStationMeteo, token):
    urlApiMeteo = buildUrlApiMeteo(metaDataStationMeteo, token)
    jsonResponse = requests.get(urlApiMeteo).json()
    temperatureValue = jsonResponse["hourly"][metaDataStationMeteo["id"]][-1]["temperature"]
    return temperatureValue

def buildUrlApiMeteo(station, token):
    return "https://www.infoclimat.fr/opendata/?method=get&format=json&stations[]=" + station["id"] + "&token=" + token

def getTokenApiMeteo():
#    client = etcd.Client(host='localhost', port=2379)
    return infoclimat.getToken()

def getMetaDataStationMeteo():
    station = {
        "id" : "07130",
        "name" : "Rennes-St Jacques"
    }
    return station
