#!/usr/bin/env python3
import os
from confluent_kafka import Consumer

KAFKA_BROKERS = os.getenv('KAFKA_BROKERS', 'localhost:9092')
DEBUG = False
AUTO_COMMIT = False

config = {
    'bootstrap.servers': KAFKA_BROKERS,
    'group.id': 'foobar.group',
    'enable.auto.commit': AUTO_COMMIT
}
if DEBUG:
    config['debug'] = 'cgrp,topic,protocol,broker'

consumer = Consumer(**config)
consumer.subscribe(['foobar'])

try:
    while True:
        msg = consumer.poll(timeout=0.1)
        if msg is None:
            continue
        if msg.error():
            continue
        message = msg.value().decode('utf-8')
        print(message)
        if AUTO_COMMIT is False:
            print("Committing consumer offsets")
            consumer.commit()
finally:
    consumer.close()
