import json
from kafka import KafkaConsumer
from config import *

consumer = KafkaConsumer(CONFIRMED_TOPIC, bootstrap_servers=BOOTSTRAP_SERVER)
total_order = total_amount = 0
logging.info("Analytics listenning ...")

# while True:
for message in consumer:
    consumed_msg = json.loads(message.value.decode())
    total_amount += float(consumed_msg['total_amount'])
    total_order += 1

    logging.info(f"Total Orders : {total_order} - Total Amount : {total_amount} $")

logging.info(f"Total Orders for today : {total_order}")
logging.info(f"Total Amount for today : {total_amount} $") 
