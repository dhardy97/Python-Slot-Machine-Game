import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# Number of rows in the slot machine
ROWS = 3
# Number of columns in the slot machine
COLS = 3

# Number of occurrences for each symbol
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# Value of each symbol
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    """
    Calculate the winnings based on the columns, winning lines, bet amount, and symbol values.

    Parameters:
    - columns: List of lists representing the result of the spin
    - lines: Number of lines bet on
    - bet: Bet amount per line
    - values: Dictionary of symbol values

    Returns:
    - winnings: Total winnings
    """
    # Initialize winnings to 0
    winnings = 0

    # For each winning line
    for line in lines:
        # Get the symbol on this line
        symbol = columns[0][line]

        # Add the value of this symbol to the winnings
        winnings += values[symbol]

    # Multiply the winnings by the bet amount
    winnings *= bet

    return winnings

def get_slot_machine_spin(rows, cols, symbols):
    """
    Generate a random spin of the slot machine.

    Parameters:
    - rows: Number of rows in the slot machine
    - cols: Number of columns in the slot machine
    - symbols: Dictionary of symbol counts

    Returns:
    - columns: List of lists representing the result of the spin
    - winning_lines: List of winning lines
    """
    # Create a list of all symbols based on their counts
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    # Generate the columns for the slot machine spin
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        # Randomly select a symbol for each row in the column
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    # Check for matching rows and add them to a list of winning lines
    winning_lines = []
    for row in range(rows):
        if len(set([column[row] for column in columns])) == 1:
            winning_lines.append(row)

    return columns, winning_lines

def print_slot_machine(columns):
    """
    Prints the slot machine to the console.

    Parameters:
    - columns: List of lists representing the result of the spin
    """
    for row in range(len(columns[0])):
        for i, col in enumerate(columns):
            if i != len(columns) - 1:
                print(col[row], end=" | ")
            else:
                print(col[row], end="")

        print()

def deposit():
    """
    Prompt the user to enter the amount to deposit.

    Returns:
    - amount: Amount deposited
    """
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a positive number.")
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
    """
    Prompt the user to enter the number of lines to bet on.

    Returns:
    - lines: Number of lines to bet on
    """
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    """
    Prompt the user to enter the bet amount per line.

    Returns:
    - bet: Bet amount per line
    """
    while True:
        bet = input("What would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return bet

def spin(balance):
    """
    Perform a spin of the slot machine.

    Parameters:
    - balance: Current balance

    Returns:
    - balance: Updated balance after the spin
    """
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print("You don't have enough money to make that bet. You have $" + str(balance) + ".")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet: ${total_bet}.")

    columns, winning_lines = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(columns)
    winnings = check_winnings(columns, winning_lines, bet, symbol_value) 
    print(f"You won ${winnings}.")
    print(f"Winning lines:", *winning_lines)
    return balance + winnings - total_bet

def main():
    """
    Main function to run the slot machine game.
    """
    balance = deposit()
    while True:
        print(f"Your balance is ${balance}.")
        answer = input("Press enter to play (q to quit).")
        if answer.lower() == "q":
            break
        balance = spin(balance)

    print(f"Your final balance is ${balance}.")

main()