import logging

# ----------- set globals -----------

BOOTSTRAP_SERVER = 'localhost:19092'
ORDER_TOPIC = 'order_details'
CONFIRMED_TOPIC = 'order_confirmed'
MAX_ORDERS = 15
ORDERS_ITEMS = [
    "Pizza", "Burger", "Salad", "Pasta", "Ice Cream", "Sushi", "Sandwich",
    "Taco", "Steak", "Chicken Wings", "Fries", "Lasagna", "Hot Dog", "Donuts"
]

# ----------- config logs -----------

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] - %(message)s', datefmt='%H:%M:%S')
