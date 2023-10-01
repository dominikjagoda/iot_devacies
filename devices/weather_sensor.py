import random
import datetime
import decimal
from typing import Dict, Any
from dataclasses import dataclass

@dataclass(frozen=True)
class WeatherSensor:
    device_id: int
    name: str
    latitude: float
    longitude: float
    
    def generate_data(self) -> Dict[str, Any]:
        """
        Generates simulated weather data for the sensor.

        Returns:
            Dict[str, Any]: A dictionary containing generated weather data, including
                  device ID, name, timestamp, location, and sensor data
                  (temperature, humidity, pressure, light intensity).
        """
        data = {
            "device_id": self.device_id,
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




