"""Bank class - holds and manages a collection of accounts."""

from account import Account, SavingsAccount, CheckingAccount
from exceptions import AccountNotFoundError, InvalidAmountError


class Bank:
    """A simple in-memory bank that owns a set of accounts."""

    def __init__(self, name: str):
        self.name = name
        self._accounts: dict[str, Account] = {}
        self._savings_count = 0
        self._checking_count = 0

    def create_account(self, owner: str, account_type: str,
                        opening_balance: float = 0.0) -> Account:
        """Create a new savings or checking account and register it."""
        if opening_balance < 0:
            raise InvalidAmountError("Opening balance cannot be negative.")

        account_type = account_type.strip().lower()

        if account_type == "savings":
            self._savings_count += 1
            number = f"SA{self._savings_count:03d}"
            account: Account = SavingsAccount(owner, number, opening_balance)
        elif account_type == "checking":
            self._checking_count += 1
            number = f"CA{self._checking_count:03d}"
            account = CheckingAccount(owner, number, opening_balance)
        else:
            raise ValueError("Account type must be 'savings' or 'checking'.")

        self.add_account(account)
        return account

    def add_account(self, account: Account) -> None:
        """Register a new account with the bank."""
        self._accounts[account.account_number] = account

    def get_account(self, account_number: str) -> Account:
        """Look up an account by its number, or raise if it doesn't exist."""
        account = self._accounts.get(account_number)
        if account is None:
            raise AccountNotFoundError(f"No account with number {account_number}.")
        return account

    def list_accounts(self) -> list[Account]:
        """Return all accounts currently held by the bank."""
        return list(self._accounts.values())

    def compare_accounts(self, number_a: str, number_b: str) -> str:
        """Return a human-readable comparison of two accounts' balances."""
        account_a = self.get_account(number_a)
        account_b = self.get_account(number_b)

        if account_a > account_b:
            return f"{account_a.owner}'s account has a larger balance."
        if account_a < account_b:
            return f"{account_b.owner}'s account has a larger balance."
        return "Both accounts have equal balances."
