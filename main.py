

from devices import WeatherSensor, insert_json_to_mongodb



devices = [
    WeatherSensor(device_id=1, name="sensor_pl", latitude=12, longitude=11),
    WeatherSensor(device_id=2, name="sensor_de", latitude=17, longitude=17),
    WeatherSensor(device_id=3, name="sensor_fr", latitude=25, longitude=25),
    WeatherSensor(device_id=4, name="sensor_it", latitude=30, longitude=34),
    WeatherSensor(device_id=5, name="sensor_en", latitude=31, longitude=43),
]

MONGO_URI = "mongodb://root:examplePassword@localhost:27017/"
DATABASE_NAME = "iot_devices"
COLLECTION_NAME = "WeatherSensor"


for device in devices:
    data = device.generate_data()
    insert_json_to_mongodb(
        json_data=data, 
        mongo_uri=MONGO_URI,
        database_name=DATABASE_NAME, 
        collection_name=COLLECTION_NAME
        )

print(data)

#insert_data_to_mongodb(data=data, mongo_host="localhost", mongo_port=27017, db="iot_devices", collection="WeatherSensor")



