"""Custom exceptions used across the banking application."""


class InsufficientFundsError(Exception):
    """Raised when a withdrawal or transfer exceeds the available balance."""


class InvalidAmountError(Exception):
    """Raised when a deposit/withdraw/transfer amount is zero or negative."""


class AccountNotFoundError(Exception):
    """Raised when a lookup for an account number finds nothing."""
