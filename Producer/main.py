import csv
import time
from datetime import datetime
from src.producerkafka import ProducerKafka


def write_messages():
    producer = ProducerKafka()
    with open('data/sample.csv', newline='', encoding='utf-8') as csvfile:
        file = csv.reader(csvfile)
        next(file)
        for row in file:
            now = datetime.now()
            date_str = now.strftime("%a %b %d %H:%M:%S %Y")
            row[3] = date_str
            message = {'author_id': row[1], 'created_at': row[3], 'text': row[4]}
            producer.send(message)
            time.sleep(0.08)

    producer.close()


if __name__ == '__main__':
    write_messages()
