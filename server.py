# server.py

from flask import Flask, jsonify, request
from accounts import get_balance, withdraw, deposit

app = Flask(__name__)


# Default route (Homepage)
@app.route('/')
def home():
    """Default route to provide API information."""
    return jsonify({"message": "Welcome to the Banking API! Use the provided endpoints to interact with the system."})

@app.route('/accounts/<account_number>/balance', methods=['GET'])
def balance(account_number):
    """Returns the balance of a given account."""
    balance = get_balance(account_number)
    if balance is None:
        return jsonify({"error": "Account not found"}), 404
    return jsonify({"account_number": account_number, "balance": balance})

@app.route('/accounts/<account_number>/withdraw', methods=['POST'])
def withdraw_money(account_number):
    """Withdraws money from an account if sufficient balance exists."""
    try:
        data = request.get_json()
        amount = data.get("amount", 0)

        if amount <= 0:
            return jsonify({"error": "Invalid amount"}), 400

        if withdraw(account_number, amount):
            return jsonify({"message": "Withdrawal successful", "amount": amount})
        else:
            return jsonify({"error": "Insufficient funds or account not found"}), 400
    except Exception:
        return jsonify({"error": "Invalid JSON format"}), 400

@app.route('/accounts/<account_number>/deposit', methods=['POST'])
def deposit_money(account_number):
    """Deposits money into an account."""
    try:
        data = request.get_json()
        amount = data.get("amount", 0)

        if amount <= 0:
            return jsonify({"error": "Invalid amount"}), 400

        if deposit(account_number, amount):
            return jsonify({"message": "Deposit successful", "amount": amount})
        else:
            return jsonify({"error": "Account not found"}), 404
    except Exception:
        return jsonify({"error": "Invalid JSON format"}), 400

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)