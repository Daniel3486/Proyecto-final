from kafka import KafkaConsumer
from pymongo import MongoClient
import json

consumer = KafkaConsumer('weather', 'nasa', bootstrap_servers='localhost:9092')
client = MongoClient('localhost', 27017)
db = client.data_pipeline

for message in consumer:
    topic = message.topic
    data = json.loads(message.value.decode('utf-8'))
    db[topic].insert_one(data)