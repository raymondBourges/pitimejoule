from fastapi import FastAPI, Response
import requests
import infoclimat as infoclimat

app = FastAPI()

@app.get("/")
async def root():
    station = {
        "id" : "07130",
        "name" : "Rennes-St Jacques"
    }
    token = infoclimat.getToken()
    urlMeteoApi = "https://www.infoclimat.fr/opendata/?method=get&format=json&stations[]=" + station["id"] + "&token=" + token
    jsonResponse = requests.get(urlMeteoApi).json()

    temperatureValue = jsonResponse["hourly"][station["id"]][-1]["temperature"]

    data = "temperature{station=\"" + station["name"] + "\"} " + temperatureValue
    return Response(content=data, media_type="text/plain")
