from kafka import KafkaProducer
import json


class ProducerKafka:
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers='kafka-server:9092',
                                      value_serializer=lambda m: json.dumps(m).encode('ascii'))

    def send(self, message):
        self.producer.send('tweets', message)
        self.producer.flush()

    def close(self):
        self.producer.close()

