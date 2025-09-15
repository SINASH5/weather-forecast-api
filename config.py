import os
from dotenv import load_dotenv

load_dotenv()  # Loads .env automatically

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
