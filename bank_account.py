import json
import os

FileName = "bank_data.json"

if not os.path.exists(FileName):
    with open(FileName, "w") as f:
        json.dump({}, f)
        
def load_data():
    try:
        with open(FileName, "r", encoding="utf-8-sig") as f:
            data = json.load(f)
            print("Loaded data:", data)  # Debugging print statemen
            return data
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return {}

def save_data(data):
    try:
        with open(FileName, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
            print("Saved data:", data)  # Debugging print statement
    except TypeError as e:
        print(f"Error saving JSON: {e}")
        
def register(username, password):
    data = load_data()
    if username in data:
        return "Username already exists"
    data[username] = {"password": password, "balance": 0}
    save_data(data)
    return "Registration successful"

def login(username, password):
    data = load_data()
    if username not in data:
        return False, "Username does not exist"
    if data[username]["password"] != password:
        return False, "Password is incorrect"
    return True, "Login successful"

def check_balance(username):
    data = load_data()
    return data[username]["balance"]

def deposit(username, amount):
    if amount <= 0:
        return "Invalid amount"
    data = load_data()
    data[username]["balance"] += amount 
    save_data(data)
    return "Deposit successful"

def withdraw(username, amount):
    if amount <= 0:
        return "Invalid amount"
    data = load_data()
    if data[username]["balance"] < amount:
        return "Insufficient balance"
    data[username]["balance"] -= amount
    save_data(data)
    return "Withdrawal successful"

username = input("Enter username: ")
password = input("Enter password: ")

logged_in, message = login(username, password)
if not logged_in:
    print(message)
    registration_message = register(username, password)
    print(registration_message)
    if registration_message == "Registration successful":
        logged_in, message = login(username, password)
        if not logged_in:
            print(message)
            exit()
else:
    print(message)

while logged_in:
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("Balance:", check_balance(username))
    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        print(deposit(username, amount))
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        print(withdraw(username, amount))
    elif choice == 4:
        break
    else:
        print("Invalid choice")