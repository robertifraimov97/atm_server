
# Dictionary to store accounts and their balances (in-memory storage)
accounts = {
    "123456": {"balance": 1000.0},  # Account with an initial balance of 1000
    "654321": {"balance": 500.0}    # Account with an initial balance of 500
}

def get_balance(account_number):
    """Returns the balance of the specified account."""
    return accounts.get(account_number, {}).get("balance", None)

def withdraw(account_number, amount):
    """Withdraws money from the account if sufficient balance is available."""
    if account_number in accounts and accounts[account_number]["balance"] >= amount:
        accounts[account_number]["balance"] -= amount
        return True
    return False

def deposit(account_number, amount):
    """Deposits a specified amount into the account if it exists."""
    if account_number in accounts:
        accounts[account_number]["balance"] += amount
        return True
    return False