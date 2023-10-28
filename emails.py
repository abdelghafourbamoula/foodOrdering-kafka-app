import json
from kafka import KafkaConsumer
from config import *

consumer = KafkaConsumer(CONFIRMED_TOPIC, bootstrap_servers=BOOTSTRAP_SERVER)
emails_set  = set()
logging.info("Email listenning ...")

# while True:
for message in consumer:
    consumed_msg = json.loads(message.value.decode())
    email = consumed_msg['customer_email']
    logging.info(f"Sending email to {email}")
    emails_set.add(email)
    logging.info(f"Email sent to {len(emails_set)} emails")
