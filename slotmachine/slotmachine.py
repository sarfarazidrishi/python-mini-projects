
def deposit():
    while True:
        amount=input("what would you like to deposit? $")
        if amount.isdigit():
            amount=int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be grater than 0")
        else:
            print("please enter a number")
    return amount

def main():
    balance= deposit()

