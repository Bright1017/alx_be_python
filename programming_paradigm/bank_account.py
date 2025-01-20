"""
0. Create a Simple Bank Account Class
mandatory
Score: 0.0% (Checks completed: 0.0%)
Objective: Understand the fundamentals of OOP in Python by implementing a BankAccount class that encapsulates banking operations. Use command line arguments to interact with instances of this class.

Task Description:
You will create two Python scripts: bank_account.py, which contains the BankAccount class, and main-0.py, which interfaces with the class through command line arguments to perform banking operations.

bank_account.py:
Class Definition:

Define a class named BankAccount.
Use the __init__ method to initialize an account_balance attribute. Optionally, accept an initial balance parameter, defaulting to zero.
Encapsulation and Behaviors:

Implement deposit(amount), withdraw(amount), and display_balance() methods.
deposit should add the specified amount to account_balance.
withdraw should deduct the amount from account_balance if funds are sufficient, returning True; otherwise, return False and do not alter the balance.
display_balance should print the current balance in a user-friendly format.


"""


# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the BankAccount with an optional initial balance.
        :param initial_balance: The starting balance of the account (default is 0).
        """
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit a specified amount into the account.
        :param amount: The amount to deposit (must be positive).
        """
        if amount > 0:
            self.__account_balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account if sufficient funds are available.
        :param amount: The amount to withdraw (must be positive).
        :return: True if the withdrawal was successful, False otherwise.
        """
        if amount > 0:
            if self.__account_balance >= amount:
                self.__account_balance -= amount
                return True
            else:
                return False
        else:
            raise ValueError("Withdrawal amount must be positive.")

    def display_balance(self):
        """
        Print the current account balance in a user-friendly format.
        """
        print(f"Current balance: ${self.__account_balance:.2f}")

    def get_balance(self):
        """
        Return the current account balance.
        :return: The current balance as a float.
        """
        return self.__account_balance