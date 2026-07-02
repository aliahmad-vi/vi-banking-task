"""Menu action: View Account Type."""

from src.bank import Bank


def view_account_type(bank: Bank) -> None:
    """Print the owner and account type for a given account number."""
    number = input("Account number: ").strip()
    account = bank.get_account(number)
    print(f"{account.account_number} belongs to {account.owner} "
          f"and is a {account.account_type} account.")
