"""Command-line interface for the banking application.

This module only handles the menu loop and routing. The actual logic
for each option lives in its own file under src/actions/.
"""

from src.bank import Bank
from src.exceptions import (
    AccountNotFoundError,
    InsufficientFundsError,
    InvalidAmountError,
)
from src.actions.create_account import create_account
from src.actions.check_balance import check_balance
from src.actions.deposit import deposit
from src.actions.withdraw import withdraw
from src.actions.transfer import transfer
from src.actions.view_account_type import view_account_type
from src.actions.compare_accounts import compare_accounts
from src.actions.show_transactions import show_transactions

MENU = """
--------------------------------
1. Create Account
2. Check Balance
3. Deposit Money
4. Withdraw Money
5. Transfer Money
6. View Account Type
7. Compare Accounts
8. Show Transactions
0. Exit
--------------------------------
"""

# maps a menu choice to the action function that handles it
ACTIONS = {
    "1": create_account,
    "2": check_balance,
    "3": deposit,
    "4": withdraw,
    "5": transfer,
    "6": view_account_type,
    "7": compare_accounts,
    "8": show_transactions,
}


def run(bank: Bank) -> None:
    """Start the interactive command-line loop."""
    print(f"Welcome to {bank.name}")

    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("Goodbye.")
            break

        action = ACTIONS.get(choice)
        if action is None:
            print("Invalid option, try again.")
            continue

        try:
            action(bank)
        except (AccountNotFoundError, InsufficientFundsError,
                InvalidAmountError, ValueError) as err:
            print(f"Error: {err}")
