"""Entry point for the banking application.
"""

from src.account import SavingsAccount, CheckingAccount
from src.bank import Bank
from src.cli import run


def seed_bank() -> Bank:
    """Create a bank with a couple of starter accounts for demo purposes."""
    bank = Bank("Vital Interaction Bank")

    bank.add_account(SavingsAccount("Ali Ahmad", "SA001", balance=10000, interest_rate=0.06))
    bank.add_account(CheckingAccount("Account 2", "CA001", balance=5000, overdraft_limit=1000))

    return bank


if __name__ == "__main__":
    run(seed_bank())
