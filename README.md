# Banking System

Week 1 - Python Task (Module 2, Part A)

A command-line banking application built with core OOP concepts:
inheritance, encapsulation, custom exceptions, and magic methods.

## Features

- Create Account (savings or checking)
- Check Balance
- Deposit Money
- Withdraw Money
- Transfer Money
- View Account Type
- Compare Accounts (which has a larger / smaller / equal balance)
- Show Transactions (full history per account)
- Two account types: `SavingsAccount` (earns interest) and
  `CheckingAccount` (allows overdraft up to a limit)

## Project structure

```
task2-banking/
├── main.py                        # entry point - seeds sample accounts, starts CLI
├── requirements.txt
├── src/
│   ├── account.py                  # Account, SavingsAccount, CheckingAccount
│   ├── bank.py                      # Bank class - manages accounts, creates new ones
│   ├── cli.py                        # menu loop, dispatches to actions/
│   ├── exceptions.py                 # custom exception types
│   ├── transaction.py                 # Transaction record (with magic methods)
│   └── actions/                        # one file per menu option
│       ├── create_account.py
│       ├── check_balance.py
│       ├── deposit.py
│       ├── withdraw.py
│       ├── transfer.py
│       ├── view_account_type.py
│       ├── compare_accounts.py
│       └── show_transactions.py
└── tests/
    └── test_account.py               # unittest suite
```

## OOP concepts used

- **Inheritance** - `SavingsAccount` and `CheckingAccount` both extend `Account`
- **Encapsulation** - `Bank` keeps its accounts dict private (`_accounts`)
- **Magic methods** - `__str__`, `__repr__`, `__eq__`, `__lt__`, `__gt__` on
  `Account`, and `__str__`/`__repr__` on `Transaction`, so objects can be
  printed and compared with normal Python operators (`account_a > account_b`)
- **Custom exceptions** - `InsufficientFundsError`, `InvalidAmountError`,
  `AccountNotFoundError` instead of generic errors

## Setup (virtual environment)

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running the app

```bash
python main.py
```

Two demo accounts are seeded on startup:
- `SA001` - Ali Ahmad, Savings, Rs 10,000
- `Account 2` - Umer Massod, Checking, Rs 5,000



## Linting

```bash
pylint src/ main.py
```

Currently rated **10.00/10**.
