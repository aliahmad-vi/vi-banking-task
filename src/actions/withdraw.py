"""Menu action: Withdraw Money."""

from src.bank import Bank


def withdraw(bank: Bank) -> None:
    """Remove money from an account, if enough balance/overdraft exists."""
    number = input("Account number: ").strip()
    amount = float(input("Amount to withdraw: "))
    account = bank.get_account(number)
    account.withdraw(amount)
    print(f"Withdrawn. New balance: Rs {account.balance:,.2f}")
