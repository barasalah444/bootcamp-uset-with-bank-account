# bootcamp-uset-with-bank-account

# Assignment: Users with Bank Accounts

A Python project demonstrating the concept of Object-Oriented Programming (OOP) **Association** by linking two classes.

## Overview
This project connects the `User` class with the `BankAccount` class. Instead of storing balance directly as an attribute in `User`, each `User` instance holds a `BankAccount` instance to handle deposits, withdrawals, and balance inquiries.

## Project Structure
* `bank_account.py`: Contains the `BankAccount` class logic for managing account balance, deposits, withdrawals, interest rates, and displaying account details.
* `user.py`: Contains the `User` class logic, imports `BankAccount`, and delegates financial actions to the associated account.

