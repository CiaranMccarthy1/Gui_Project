# .venv\Scripts\activate

# This file was all done by Ciaran

# Python imports
from flask import Flask, render_template, request, redirect, url_for, session
import os
import json

# Intiates flask server
app = Flask(__name__)
app.secret_key = "Gui_project"

# Dictionary to store menu items
FOOD_MENU = [
    {"id": 1, "name": "Burger 🍔", "price": 5.99},
    {"id": 2, "name": "12' Pizza 🍕", "price": 11.99},
    {"id": 3, "name": "Hot-dog 🌭", "price": 5.99},
    {"id": 4, "name": "Fries 🍟", "price": 3.99},
    {"id": 5, "name": "Pasta 🍝", "price": 9.99},
    {"id": 6, "name": "Salad 🥗", "price": 5.99},
    {"id": 7, "name": "Tacos 🌮", "price": 4.99},
    {"id": 8, "name": "Ramen 🍜", "price": 11.99},
    {"id": 9, "name": "Sushi 🍣", "price": 5.99},
    {"id": 10, "name": "Ice-cream 🍦", "price": 2.99},
    {"id": 11, "name": "Coke 🥤", "price": 2.99},
    {"id": 12, "name": "Milk 🥛", "price": 1.99},
]


# Directory that stores user's baskets
BASKETS_DIR = "baskets"
os.makedirs(BASKETS_DIR, exist_ok=True) # Checks if directory exists

'''
Renders index.html file
If user not logged in it redirects you to the login page
Passes in menu and username to web page
'''
@app.route('/')
def index():
    if "username" not in session:
        return redirect("/login")
    return render_template("index.html", menu=FOOD_MENU, username=session.get("username"))

'''
Adds the food and drink to users basket and appends it to the file
Reloads index page
'''
@app.route("/order", methods=['POST'])
def order():
    if 'username' not in session: # Checks if user is not signed in again 
        return redirect('/login')
    food_id = int(request.form["food_id"])
    item = next((f for f in FOOD_MENU if f['id'] == food_id), None) # Loops through menu and checks if food in basket is in menu
    if item:
        basket_path = os.path.join(BASKETS_DIR, f"{session["username"]}.txt")
        with open(basket_path, "a") as f:
            f.write(json.dumps(item) + '\n') 
    return redirect("/")


'''
Renders the basket page
Reads the users file and displays the users basket
Gets the total price of basket
'''
@app.route("/basket")
def basket():
    if "username" not in session:
        return redirect("/")
    basket_path = os.path.join(BASKETS_DIR, f"{session["username"]}.txt")
    items = []
    if os.path.exists(basket_path):
        with open(basket_path) as f:
            for line in f:
                items.append(json.loads(line.strip()))
    total = sum(item["price"] for item in items)
    return render_template('basket.html', basket=items, total=total, username=session["username"])

'''
Empties the basket when after checking out
'''
@app.route("/checkout")
def checkout():
    if "username" in session:
        basketPath = os.path.join(BASKETS_DIR, f"{session["username"]}.txt")
        if os.path.exists(basketPath):
            os.remove(basketPath)
    return render_template('checkout.html', username=session.get("username"))


'''
When receives Post request asks user to input name
'''
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        return redirect("/")    
    return render_template("login.html")

'''
Allows user to logout
'''
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/login")


'''
Allows user to remove item from basket
Gets index of item being removed and removes line from file
'''
@app.route("/remove", methods=["POST"])
def remove():
    if "username" not in session:
        return redirect("/")
    
    index = int (request.form["index"])
    basketPath = os.path.join(BASKETS_DIR, f"{session["username"]}.txt")

    if os.path.exists(basketPath):
        with open(basketPath) as f:
            lines = f.readlines()
        if 0 <= index < len(lines):
            del lines[index]
            with open(basketPath, "w") as f:
                f.writelines(lines)
    return redirect("/basket")

@app.route("/about")
def about():
    return render_template("about.html", username=session.get("username"))
''' 
runs app
'''
if __name__ == "__main__":
    app.run()

'''
Reference 

https://www.geeksforgeeks.org/flask-tutorial/
https://flask.palletsprojects.com/en/stable/#user-s-guide
https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
'''
