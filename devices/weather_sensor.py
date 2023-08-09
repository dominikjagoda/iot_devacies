import random
import datetime
import decimal


class WeatherSensor:

    def __init__(self, id: int, name: str, latitude: float, longitude: float):

        self._id = id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    @property
    def id(self):
        return self._id
    
    def generate_data(self) -> dict:

        data = {
            "device_id": self._id,
            "name": self.name,
            "timestamp": datetime.datetime.now(),
            "location": {
            "latitude": self.latitude,
            "longitude": self.longitude
            }, 
            "sensor_data": {
            "temperature": float(decimal.Decimal(random.randrange(-300, 500))/100),
            "humidity": float(decimal.Decimal(random.randrange(0, 100))/100),
            "pressure": float(decimal.Decimal(random.randrange(9000, 11000))/100),
            "light_intensity": random.randrange(500, 5000),
            }
        }

        return data






