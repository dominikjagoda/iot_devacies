
import time
from devices import WeatherSensor
from fastapi import FastAPI


devices = [
    WeatherSensor(id=1, name="sensor_pl", latitude=12, longitude=11),
    WeatherSensor(id=2, name="sensor_de", latitude=17, longitude=17),
    WeatherSensor(id=3, name="sensor_fr", latitude=25, longitude=25),
    WeatherSensor(id=4, name="sensor_it", latitude=30, longitude=34),
    WeatherSensor(id=5, name="sensor_en", latitude=31, longitude=43),
]

app = FastAPI()

@app.get("/")
def root():
    return [ device.generate_data() for device in devices ]