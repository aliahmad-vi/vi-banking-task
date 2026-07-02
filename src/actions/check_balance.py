"""Menu action: Check Balance."""

from src.bank import Bank


def check_balance(bank: Bank) -> None:
    """Print the current balance of a given account."""
    number = input("Account number: ").strip()
    account = bank.get_account(number)
    print(f"Balance: Rs {account.balance:,.2f}")
