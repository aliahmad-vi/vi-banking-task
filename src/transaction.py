"""Transaction record used to keep a history on each account."""

from datetime import datetime


class Transaction:
    """A single logged action (deposit/withdraw/transfer) on an account."""

    def __init__(self, kind: str, amount: float, balance_after: float):
        self.kind = kind
        self.amount = amount
        self.balance_after = balance_after
        self.timestamp = datetime.now()

    def __str__(self) -> str:
        stamp = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        return (
            f"{stamp} | {self.kind:<12} | amount: {self.amount:>10,.2f} "
            f"| balance after: {self.balance_after:>10,.2f}"
        )

    def __repr__(self) -> str:
        return (
            f"Transaction(kind={self.kind!r}, amount={self.amount!r}, "
            f"balance_after={self.balance_after!r})"
        )
