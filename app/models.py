from pydantic import BaseModel

class CityRequest(BaseModel):
    city: str  # Input: city name

class WeatherResponse(BaseModel):
    temperature: float
    humidity: int
    description: str
