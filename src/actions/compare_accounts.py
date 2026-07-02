"""Menu action: Compare Accounts."""

from src.bank import Bank


def compare_accounts(bank: Bank) -> None:
    """Print which of two accounts has the larger balance."""
    number_a = input("First account number: ").strip()
    number_b = input("Second account number: ").strip()
    print(bank.compare_accounts(number_a, number_b))
