from fastapi import FastAPI, HTTPException
from app.weather_service import get_weather
from pydantic import BaseModel

app = FastAPI()

class CityRequest(BaseModel):
    city: str

@app.get("/")
def root():
    return {"message": "API is up!"}

@app.post("/forecast/")
def forecast(city_request: CityRequest):
    result = get_weather(city_request.city)

    if "error" in result:
        # Raise proper HTTP error
        raise HTTPException(status_code=404, detail=result["error"])
    
    return result
