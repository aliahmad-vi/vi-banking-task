"""Menu action: Create Account."""

from src.bank import Bank


def create_account(bank: Bank) -> None:
    """Prompt for owner/type/opening balance and register a new account."""
    owner = input("Owner name: ").strip()
    account_type = input("Account type (savings/checking): ").strip()
    opening_balance = float(input("Opening balance: ") or 0)

    account = bank.create_account(owner, account_type, opening_balance)
    print(f"Account created: {account.account_number}")
