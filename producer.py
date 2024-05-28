import requests
import json
from kafka import KafkaProducer

def get_data_from_api(url):
    response = requests.get(url)
    return response.json()

def produce_message(producer, topic, message):
    producer.send(topic, json.dumps(message).encode('utf-8'))

producer = KafkaProducer(bootstrap_servers='localhost:9092')

nasa_url = 'https://api.nasa.gov/planetary/apod?api_key=NIVD6p4e3GEMCGtGbbj0uOlTfJfOtuILfuoF7fdF'
nasa_data = get_data_from_api(nasa_url)
produce_message(producer, 'nasa', nasa_data)

weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=London&appid=fb49191e8566d997d01e6e812eab3a08'
weather_data = get_data_from_api(weather_url)
produce_message(producer, 'weather', weather_data)


nasa_url = 'https://api.nasa.gov/planetary/apod?api_key=NIVD6p4e3GEMCGtGbbj0uOlTfJfOtuILfuoF7fdF'
nasa_data = get_data_from_api(nasa_url)
produce_message(producer, 'nasa', nasa_data)



