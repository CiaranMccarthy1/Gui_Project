from flask import *

app = Flask(__name__)

menu = [
    {"id": 1, "name": "Burger", "price": 9.99},
    {"id": 2, "name": "Pizza", "price": 14.99},
    {"id": 3, "name": "Coke", "price": 2.50},
]

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
