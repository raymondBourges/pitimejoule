from fastapi import FastAPI, Response
import requests, os
import etcd3 # pip install etcd3 + pip install protobuf==3.20

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
    #lecture du token depuis la base ETCD
    etcd = etcd3.client(os.environ['ETCD_HOST'], os.environ['ETCD_PORT'])
    return etcd.get("/fastapi/tokenApiMeteo")[0].decode('utf-8')

def getMetaDataStationMeteo():
    station = {
        "id" : "07130",
        "name" : "Rennes-St Jacques"
    }
    return station
