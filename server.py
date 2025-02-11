# server.py

from flask import Flask, jsonify, request
from accounts import get_balance, withdraw, deposit

app = Flask(__name__)

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
    data = request.json
    amount = data.get("amount", 0)

    if amount <= 0:
        return jsonify({"error": "Invalid amount"}), 400

    if withdraw(account_number, amount):
        return jsonify({"message": "Withdrawal successful", "amount": amount})
    else:
        return jsonify({"error": "Insufficient funds or account not found"}), 400

@app.route('/accounts/<account_number>/deposit', methods=['POST'])
def deposit_money(account_number):
    """Deposits money into an account."""
    data = request.json
    amount = data.get("amount", 0)

    if amount <= 0:
        return jsonify({"error": "Invalid amount"}), 400

    if deposit(account_number, amount):
        return jsonify({"message": "Deposit successful", "amount": amount})
    else:
        return jsonify({"error": "Account not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)