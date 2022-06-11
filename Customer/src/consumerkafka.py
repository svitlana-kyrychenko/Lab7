import csv
from datetime import datetime
from kafka import KafkaConsumer
import json


class ConsumerKafka:
    def __init__(self):
        self.consumer = consumer = KafkaConsumer('tweets', bootstrap_servers= 'kafka-server:9092',
                                                 value_deserializer=lambda x: json.loads(x.decode('utf-8')))
        previous_created_at = None
        is_first = True
        tweets = []

        for message in consumer:
            author_id = message.value["author_id"]
            created_at_file_write = datetime.strftime(
                datetime.strptime(message.value['created_at'], "%a %b %d %H:%M:%S %Y"), "%d_%m_%Y_%H_%M")
            created_at_str = datetime.strftime(
                datetime.strptime(message.value['created_at'], "%a %b %d %H:%M:%S %Y"), "%a %b %d %H:%M %Y")
            text = message.value["text"]

            if is_first:
                previous_created_at = created_at_file_write
                tweets.append([author_id, created_at_str, text])
                is_first = False
            elif previous_created_at == created_at_file_write:
                tweets.append([author_id, created_at_str, text])
            else:

                with open(
                        f'tweets_files/tweets_{previous_created_at}.csv',
                        'w') as f:
                    writer = csv.writer(f)
                    [writer.writerow(row) for row in tweets]

                previous_created_at = created_at_file_write
                tweets = [[author_id, created_at_str, text]]

        self.consumer.close()


