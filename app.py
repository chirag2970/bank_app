from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

balance = 0  # temporary (later move to database)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/deposit", methods=["POST"])
def deposit():
    global balance
    amount = float(request.json["amount"])
    balance += amount
    return jsonify({"message": f"Deposited {amount}", "balance": balance})

@app.route("/withdraw", methods=["POST"])
def withdraw():
    global balance
    amount = float(request.json["amount"])
    if amount > balance:
        return jsonify({"error": "Insufficient funds", "balance": balance}), 400
    balance -= amount
    return jsonify({"message": f"Withdrew {amount}", "balance": balance})

@app.route("/balance", methods=["GET"])
def get_balance():
    return jsonify({"balance": balance})

if __name__ == "__main__":
    app.run(debug=True)
