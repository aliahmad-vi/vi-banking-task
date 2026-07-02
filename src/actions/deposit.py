"""Menu action: Deposit Money."""

from src.bank import Bank


def deposit(bank: Bank) -> None:
    """Add money to an account."""
    number = input("Account number: ").strip()
    amount = float(input("Amount to deposit: "))
    account = bank.get_account(number)
    account.deposit(amount)
    print(f"Deposited. New balance: Rs {account.balance:,.2f}")
