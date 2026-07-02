"""Menu action: Transfer Money."""

from src.bank import Bank


def transfer(bank: Bank) -> None:
    """Move money from one account to another."""
    from_number = input("From account number: ").strip()
    to_number = input("To account number: ").strip()
    amount = float(input("Amount to transfer: "))

    from_account = bank.get_account(from_number)
    to_account = bank.get_account(to_number)
    from_account.transfer(to_account, amount)
    print(f"Transferred Rs {amount:,.2f} from {from_number} to {to_number}.")
