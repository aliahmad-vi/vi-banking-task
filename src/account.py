"""Account classes for the banking application.

Defines a base Account class along with two specialised account types
(SavingsAccount, CheckingAccount) that demonstrate inheritance, and a
handful of magic methods that let accounts be printed, compared, and
checked for equality in a natural way.
"""

from exceptions import InsufficientFundsError, InvalidAmountError
from transaction import Transaction


class Account:
    """A basic bank account tied to a single owner."""

    def __init__(self, owner: str, account_number: str, balance: float = 0.0):
        self.owner = owner
        self.account_number = account_number
        self.balance = float(balance)
        self.account_type = "Generic"
        self.transactions: list[Transaction] = []

    def deposit(self, amount: float) -> None:
        """Add money to the account."""
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive.")
        self.balance += amount
        self.transactions.append(Transaction("Deposit", amount, self.balance))

    def withdraw(self, amount: float) -> None:
        """Remove money from the account, if enough balance exists."""
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw {amount:.2f}, balance is only {self.balance:.2f}."
            )
        self.balance -= amount
        self.transactions.append(Transaction("Withdrawal", amount, self.balance))

    def transfer(self, other: "Account", amount: float) -> None:
        """Move money from this account into another account."""
        self.withdraw(amount)
        other.deposit(amount)

    # ---- magic methods ----

    def __str__(self) -> str:
        return (
            f"[{self.account_type}] {self.account_number} - {self.owner} "
            f"- Rs {self.balance:,.2f}"
        )

    def __repr__(self) -> str:
        return (
            f"Account(owner={self.owner!r}, account_number={self.account_number!r}, "
            f"balance={self.balance!r})"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Account):
            return NotImplemented
        return self.balance == other.balance

    def __lt__(self, other: "Account") -> bool:
        return self.balance < other.balance

    def __gt__(self, other: "Account") -> bool:
        return self.balance > other.balance


class SavingsAccount(Account):
    """A savings account that can earn interest on its balance."""

    def __init__(self, owner: str, account_number: str, balance: float = 0.0,
                 interest_rate: float = 0.05):
        super().__init__(owner, account_number, balance)
        self.account_type = "Savings"
        self.interest_rate = interest_rate

    def apply_interest(self) -> None:
        """Credit the account with interest based on its current balance."""
        self.balance += self.balance * self.interest_rate


class CheckingAccount(Account):
    """A checking account that allows withdrawing beyond zero, up to a limit."""

    def __init__(self, owner: str, account_number: str, balance: float = 0.0,
                 overdraft_limit: float = 500.0):
        super().__init__(owner, account_number, balance)
        self.account_type = "Checking"
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: float) -> None:
        """Allow withdrawals to dip into the overdraft limit."""
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive.")
        if amount > self.balance + self.overdraft_limit:
            raise InsufficientFundsError(
                f"Cannot withdraw {amount:.2f}, available with overdraft is "
                f"{self.balance + self.overdraft_limit:.2f}."
            )
        self.balance -= amount
        self.transactions.append(Transaction("Withdrawal", amount, self.balance))
