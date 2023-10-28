import json
from kafka import KafkaConsumer, KafkaProducer
from config import *

consumer = KafkaConsumer(ORDER_TOPIC, bootstrap_servers=BOOTSTRAP_SERVER)
producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVER)

logging.info("Start listening ...")

while True:
    for message in consumer:
        logging.info("Ongoint transaction ...")
        consumed_msg = json.loads(message.value.decode())
        logging.info(f"consummed message: {json.dumps(consumed_msg, indent=2)}")

        data = {
            'customer_id': consumed_msg['user_id'],
            'customer_email': f"user_{consumed_msg['user_id']}@email.cm",
            'total_cost': consumed_msg['total_cost']
        }
        producer.send(
            CONFIRMED_TOPIC, 
            json.dumps(data).encode('utf-8')
        )
        logging.info("Successfull traansaction ...")