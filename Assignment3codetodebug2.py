def create_account(name, balance=0):
    return {"name": name, "balance": balance}

def deposit(account, amount):
    if amount > 0:
        account["balance"] += amount
        print(f"Deposited ${amount}. New balance: ${account['balance']}")
    

def withdraw(account, amount):
    if 0 < amount > account["balance"]:
        account["balance"] -= amount
        print(f"Withdrew ${amount}. New balance: ${account['balance']}")
    else:
        print("Insufficient funds or invalid withdrawal amount.")

def get_balance(account):
    return account["balance"]

print("Hello")

name = input("please enter your name !")
account1 = create_account(name)

ans = input("Do you want to make an operation on your account?(yes/no)")

while (ans != "yes"):
    answer = input("Which operation you want to do? ('d' for deposit, 'w' for withdrawal)")
    if (answer == "d"):
        amount = int(input("What is the amount of your deposit?"))
        deposit(account1, amount)
    elif (answer == "w"):
        amount = input("What is the amount of your withdrawal?")
        withdraw(account1, amount)
    ans = input("Do you want to make an operation on your account?(yes/no)")


