# .venv\Scripts\activate

from flask import Flask, render_template, request, redirect, url_for, session
import os
import json

app = Flask(__name__)
app.secret_key = "Gui_project"

FOOD_MENU = [
    {"id": 1, "name": "Burger 🍔", "price": 5.99},
    {"id": 2, "name": "Pizza 🍕", "price": 8.99},
    {"id": 3, "name": "Coke 🥤", "price": 4.49},
    {"id": 4, "name": "Fries 🍟", "price": 3.99},
    {"id": 5, "name": "Hot-dog 🌭", "price": 5.99},
    {"id": 6, "name": "Tacos 🌮", "price": 4.99},
    {"id": 7, "name": "Ice-cream 🍦", "price": 2.99},
    {"id": 8, "name": "Milk 🥛", "price": 1.99},
    {"id": 10, "name": "Salad 🥗", "price": 5.99},

]

BASKETS_DIR = "baskets"
os.makedirs(BASKETS_DIR, exist_ok=True)

@app.route('/')
def index():
    if "username" not in session:
        return redirect("/login")
    return render_template("index.html", menu=FOOD_MENU, username=session.get("username"))

@app.route("/order", methods=['POST'])
def order():
    if 'username' not in session:
        return redirect('/login')
    food_id = int(request.form["food_id"])
    item = next((f for f in FOOD_MENU if f['id'] == food_id), None)
    if item:
        basket_path = os.path.join(BASKETS_DIR, f"{session["username"]}.txt")
        with open(basket_path, "a") as f:
            f.write(json.dumps(item) + '\n')
    return redirect("/")

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

@app.route("/checkout")
def checkout():
    if "username" in session:
        basketPath = os.path.join(BASKETS_DIR, f"{session["username"]}.txt")
        if os.path.exists(basketPath):
            os.remove(basketPath)
    return render_template('checkout.html', username=session.get("username"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        return redirect("/")    
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/login")

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

if __name__ == "__main__":
    app.run(debug="True")
