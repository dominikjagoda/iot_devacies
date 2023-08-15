import random
import datetime
import decimal
from typing import Dict, Any


class WeatherSensor:

    def __init__(self, id: int, name: str, latitude: float, longitude: float):
        
        """
        Initializes a WeatherSensor instance.

        Args:
            id (int): The unique identifier for the weather sensor.
            name (str): The name of the weather sensor.
            latitude (float): The latitude coordinate of the sensor's location.
            longitude (float): The longitude coordinate of the sensor's location.
        """

        self._id = id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    @property
    def id(self):
        """Sets id parameter as read only"""
        return self._id
    
    def generate_data(self) -> Dict[str, Any]:
        """
        Generates simulated weather data for the sensor.

        Returns:
            Dict[str, Any]: A dictionary containing generated weather data, including
                  device ID, name, timestamp, location, and sensor data
                  (temperature, humidity, pressure, light intensity).
        """
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






