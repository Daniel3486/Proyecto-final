import matplotlib.pyplot as plt
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.data_pipeline

weather_data = list(db.weather.find())
nasa_data = list(db.nasa.find())


temperatures = [item['main']['temp'] for item in weather_data]

plt.figure(figsize=(10, 5))
plt.plot(temperatures)
plt.title('Temperaturas de OpenWeather')
plt.xlabel('Muestras')
plt.ylabel('Temperatura (K)')
plt.show()
