import random
from itertools import groupby

MAX_LINES = 3
MAX_BET = 500
MIN_BET = 1
COLS = 3
ROWS = 3

symbol_counts = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_values = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}


def check_winnings(columns,lines,values,bet):
    winnings = 0
    winning_lines = []
    for i, column in enumerate(columns):
        g =groupby(column)
        bingo = next(g,True) and not next(g, False)
        if i+1 in range(1,lines+1) and bingo:
            symbol = column[i]
            winnings +=  values[symbol] * bet
            winning_lines.append(i+1)
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column =[]
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
            for i, column in enumerate(columns):
                for j in range(len(column)):
                    print(column[j], end=" | ")

                print("")
def deposit():
    while True:
        amount = input("what whould you like to deposit ?")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero")
        else:
            print("Please enter a number")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Choose the number of lines you would bet on between 1 and " + str(MAX_LINES))
        if lines.isdigit():
            lines = int(lines)
            if lines >= 1 and lines <= MAX_LINES:
                break
            else:
                print("lines must be greater than 1 and inferior to "+ str(MAX_LINES))
        else:
            print("Please enter a number")
    return lines

def getBet():
    while True:
        bet = input("How much do you wanna bet? between " + str(MIN_BET) + " to " + str(MAX_BET))
        if bet.isdigit():
            bet = int(bet)
            if bet >= MIN_BET and bet <= MAX_BET:
                break
            else:
                print(f"the bet should bet betwenn {MIN_BET} - {MAX_BET}")
        else:
            print("Please enter a number")
    return bet

def game():
    balance = deposit()
    while True:
        i = input("press q to quit and enter to play")
        if i == "q":
            break

        lines = get_number_of_lines()
        while True:
            bet = getBet()
            totalBet = bet * lines

            if totalBet <= balance:
                balance = balance - totalBet
                break
            else:
                print(f"Not enough credit in your balance. You have ${balance} trying to bet {totalBet}")

        print(f"You are betting ${totalBet}")

        slots = get_slot_machine_spin(ROWS, COLS, symbol_counts)
        print_slot_machine(slots)
        winnings, winning_lines = check_winnings(slots, lines, symbol_values, totalBet)
        if winnings:
            balance += winnings
            print(f"You won ${winnings}")
            print(f"the winning lines are :", *winning_lines)
        else:
            print("sorry try next time")

        print(f"You have ${balance} in your balance")

    print(f"you left with {balance}")
if __name__ == '__main__':
    game()

