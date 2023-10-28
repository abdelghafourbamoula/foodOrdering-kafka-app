import json
import time
import random
import uuid
from kafka import KafkaProducer, producer
from config import *

logging.info("Will Generate orders evert 10 seconds")

producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVER)

for i in range(1, MAX_ORDERS):
    data = {
        'order_id': str(uuid.uuid4())[:8],
        'user_id': str(uuid.uuid4())[:8],
        'total_cost': random.randint(0, 100),
        "items": [ORDERS_ITEMS[random.randint(0, len(ORDERS_ITEMS)-1)] for _ in range(random.randint(1, 5))]
    }
    logging.info(f"Sending {i} data ...")
    producer.send(
        ORDER_TOPIC,
        json.dumps(data).encode('utf-8')
    )
    time.sleep(5)



