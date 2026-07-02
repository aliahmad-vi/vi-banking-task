"""Menu action: Show Transactions."""

from src.bank import Bank


def show_transactions(bank: Bank) -> None:
    """Print the full transaction history of an account."""
    number = input("Account number: ").strip()
    account = bank.get_account(number)

    if not account.transactions:
        print("No transactions yet on this account.")
        return

    print(f"Transaction history for {account.account_number}:")
    for txn in account.transactions:
        print(txn)
