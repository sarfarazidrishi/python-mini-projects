# import random
# max_lines=3
# min_bet=1
# max_bet=100

# rows=3 #number of rows in slot machine
# cols=3 #number of cols in slot machine

# symbol_count={
#     "A":2,
#     "B":4,
#     "C":6,
#     "D":8
# }

# def get_slot_machine_spin(rows, cols, symbols):
#     all_symbols=[]
#     for symbol, symbols_count in symbols.items():
#         for _ in range(symbols_count):
#             all_symbols.append(symbol)
            
#     columns=[]
#     for _ in range(cols):
#         columns=[]
#         current_symbols=all_symbols[:]
#         for _ in range(cols):
#             value=random.choice(all_symbols)
#             current_symbols.remove(value)
#             columns.append(value)
        
#         columns.append(columns)
#     return columns

# def print_slot_machine(columns):
#     for row in range(len(columns[0])):
#         for i, column in enumerate(columns):
#             if i !=len(columns) -1:
#                 print(columns[row], end="|")
#             else:
#                 print(columns[row], end="|")
 
# def deposit():
#     while True:
#         amount=input("how much would you like to deposit? $")
#         if amount.isdigit():
#             amount=int(amount)
#             if amount > 0:
#                 break
#             else:
#                 print("Amount must be grater than 0")
#         else:
#             print("please enter a number")
#     return amount

    
# def get_number_of_lines():
#     while True:
#         lines=input(f"Enter the number of lines to bet on 1-{max_lines}: ")
#         if lines.isdigit():
#             lines=int(lines)
#             if 1<= lines <=max_lines:
#                 break
#             else:
#                 print(f"lines must be between 1 to {max_lines}")
#         else:
#             print("please enter a number")
#     return lines

# def get_bet():
#     while True:
#         bet=input(f"Enter bet amount between {min_bet} to {max_bet}: ")
#         if bet.isdigit():
#             bet=int(bet)
#             if min_bet<= bet <= max_bet:
#                 break
#             else:
#                 (f"print betting amount should be between {min_bet} to {max_bet}")
#         else:
#             print(f"Enter only digits")
#     return bet
                

# def main():
#     balance= deposit()
#     lines=get_number_of_lines()
#     while True:
#         bet=get_bet()
#         if balance < bet*lines:
#             print(f"your bet amount must be less than your total amount that is {balance} you are trying to bet {bet*lines}")
#         else:
#             break
#     print(f"you are betting {bet} in {lines} so total bet is {bet*lines}")
#     slots=get_slot_machine_spin(rows, cols, symbol_count)
#     print_slot_machine(slots)
    
# main()

import random

max_lines = 3
min_bet = 1
max_bet = 100

rows = 3  # number of rows in slot machine
cols = 3  # number of cols in slot machine

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbols_value={
    "A":2,
    "B":4,
    "C":3,
    "D":2
}

def checkwinnig(columns, lines, bet, values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winning_lines.append(line+1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        #make all_symbols = ["A", "A", "B", "B", "B", "B", "c", "c", "c", "c", "c", "c", "D", "D", "D","D","D","D", "D", "D"]
        all_symbols.extend([symbol] * symbol_count) 
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])

def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{max_lines}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= max_lines:
                break
            else:
                print(f"Lines must be between 1 and {max_lines}.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        bet = input(f"Enter bet amount between ${min_bet} and ${max_bet}: ")
        if bet.isdigit():
            bet = int(bet)
            if min_bet <= bet <= max_bet:
                break
            else:
                print(f"Betting amount should be between ${min_bet} and ${max_bet}.")
        else:
            print("Please enter only digits.")
    return bet

def main():
    balance=deposit()
    while True:
        print(f"current balance is ${balance}")
        spin = input("press enter to spin (q to quit)")
        if spin == "q":
            break
        balance=spin()
    print("you left with  ${balance}")

def spin():
    balance = deposit()
    lines = get_number_of_lines()
    total_bet=bet * lines
    while True:
        bet = get_bet()
        if balance < bet * lines:
            print(f"Your bet amount must be less than your total amount, which is ${balance}. You are trying to bet ${bet * lines}.")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines, so the total bet is ${bet * lines}.")
    
    slots = get_slot_machine_spin(rows, cols, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines=checkwinnig(slots, lines, bet, symbols_value)
    print(f"you won ${winnings}", end="")
    print(f" you won on lines {winning_lines}")
    return winning_lines-total_bet
main()
