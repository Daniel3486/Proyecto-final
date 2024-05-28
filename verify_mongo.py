from pymongo import MongoClient

# Conectar a MongoDB
client = MongoClient('localhost', 27017)
db = client.data_pipeline

# Verificar colección de clima
print("Datos de clima (weather):")
weather_data = list(db.weather.find())
for item in weather_data:
    print(item)

# Verificar colección de NASA
print("\nDatos de NASA (nasa):")
nasa_data = list(db.nasa.find())
for item in nasa_data:
    print(item)

